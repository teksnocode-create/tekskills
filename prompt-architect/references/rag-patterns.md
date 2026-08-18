# RAG Patterns — Retrieval-Augmented Generation

> Référence satellite du skill prompt-architect v2.2
> Cas d'usage : prompts qui interrogent une base documentaire (knowledge base, embeddings, vector store)

---

## Quand utiliser cette référence

Activer quand le prompt doit :
- Interroger des documents spécifiques (et non les connaissances générales du LLM)
- Réduire les hallucinations par ancrage documentaire
- Fonctionner dans un pipeline RAG (LangChain, LlamaIndex, Claude Projects, Supabase pgvector, Pinecone, etc.)

---

## Architecture RAG — rappel

```
[Documents] → Chunking → Embedding → Vector Store
                                          ↓
[User Query] → Embedding → Similarity Search → Top-K Chunks
                                                     ↓
                                          [LLM + Chunks] → Réponse sourcée
```

**4 étapes** :
1. **Ingestion** : documents découpés en chunks (taille optimale : 500-1000 tokens avec overlap 10-20%)
2. **Indexation** : chaque chunk → vecteur via modèle d'embedding
3. **Retrieval** : question utilisateur → vecteur → recherche similarité → top-K chunks
4. **Generation** : LLM génère une réponse basée sur les chunks récupérés

---

## Patterns de prompts RAG

### Pattern 1 — RAG Standard (Question-Answering)

Le plus courant. L'utilisateur pose une question, le système récupère les chunks pertinents et génère une réponse.

```xml
<identity>
Tu es un assistant expert qui répond UNIQUEMENT à partir des documents fournis.
</identity>

<context>
{{retrieved_chunks}}
</context>

<rules>
- Réponds UNIQUEMENT en te basant sur les documents ci-dessus.
- Si l'information n'est pas dans les documents, dis-le explicitement : "Cette information n'est pas disponible dans les documents fournis."
- Cite tes sources entre crochets : [Document X, section Y].
- Ne complète JAMAIS avec des connaissances externes.
</rules>

<question>
{{user_query}}
</question>

<output_format>
Réponse concise + citations [source] après chaque affirmation clé.
</output_format>
```

### Pattern 2 — RAG Synthèse (Multi-Documents)

Quand la réponse nécessite de croiser plusieurs documents.

```xml
<identity>
Tu es un analyste qui synthétise l'information de plusieurs sources documentaires.
</identity>

<documents>
{{retrieved_chunks}}
</documents>

<task>
1. Lis attentivement TOUS les documents fournis.
2. Identifie les points de convergence entre les sources.
3. Signale les contradictions éventuelles entre documents.
4. Produis une synthèse structurée répondant à : {{user_query}}
</task>

<output_format>
## Synthèse
[Réponse intégrée avec citations]

## Points de convergence
[Ce sur quoi les sources s'accordent]

## Contradictions détectées
[Si applicable — sinon "Aucune contradiction détectée"]

## Sources utilisées
[Liste des documents cités]
</output_format>
```

### Pattern 3 — RAG Conversationnel (Multi-tours)

Pour chatbots documentaires avec historique de conversation.

```xml
<identity>
Tu es un assistant documentaire conversationnel. Tu réponds à partir de la base de connaissances et tu maintiens le contexte de la conversation.
</identity>

<knowledge_base>
{{retrieved_chunks}}
</knowledge_base>

<conversation_history>
{{chat_history}}
</conversation_history>

<rules>
- Utilise l'historique pour comprendre les références implicites (pronoms, "le même", "comme avant").
- Si la question actuelle fait référence à un échange précédent, reformule-la internement avant de chercher.
- Signale quand tu n'as plus d'information pertinente dans la base.
</rules>

<current_question>
{{user_query}}
</current_question>
```

### Pattern 4 — RAG Critique (Vérification factuelle)

Pour vérifier des affirmations contre une base documentaire (fact-checking, compliance, audit).

```xml
<identity>
Tu es un vérificateur factuel. Tu compares les affirmations à la base documentaire.
</identity>

<reference_documents>
{{retrieved_chunks}}
</reference_documents>

<claim_to_verify>
{{affirmation_a_verifier}}
</claim_to_verify>

<task>
Pour chaque affirmation :
1. Cherche la preuve dans les documents.
2. Attribue un verdict :
   - ✅ CONFIRMÉ — preuve trouvée [citation]
   - ⚠️ PARTIELLEMENT CONFIRMÉ — preuve partielle [citation + ce qui manque]
   - ❌ CONTREDIT — le document dit le contraire [citation contradictoire]
   - ❓ NON VÉRIFIABLE — aucune information pertinente dans les documents
</task>
```

---

## Anti-patterns RAG

| Anti-pattern | Problème | Solution |
|-------------|----------|----------|
| Chunks trop grands (>2000 tokens) | Bruit, contexte dilué | Réduire à 500-1000 tokens + overlap |
| Pas de citation exigée | Hallucination invisible | Exiger `[source]` après chaque affirmation |
| Top-K trop élevé (>10) | Contexte pollué par chunks non pertinents | Limiter à 3-5 + filtrage par score de similarité (>0.7) |
| Pas de fallback "je ne sais pas" | L'IA invente quand les chunks sont insuffisants | Règle explicite : "Si pas dans les docs, dis-le" |
| Mélange connaissances internes + chunks | Sources traçables impossibles | Interdire explicitement les connaissances externes |
| Pas de reformulation de query | Questions vagues → mauvais retrieval | Ajouter un module de query rewriting avant le retrieval |

---

## Paramètres d'optimisation

| Paramètre | Valeur recommandée | Impact |
|-----------|--------------------|--------|
| Chunk size | 500-1000 tokens | Précision du retrieval |
| Overlap | 10-20% du chunk | Continuité contextuelle |
| Top-K | 3-5 chunks | Balance signal/bruit |
| Similarity threshold | >0.7 | Filtrage des chunks non pertinents |
| Temperature LLM | 0.0-0.2 | Fidélité aux sources (pas de créativité) |
| Max tokens réponse | Adapter au cas | Éviter troncature |

---

## Intégration workflow (Make/n8n)

```json
{
  "module_1_query_rewrite": {
    "role": "Reformuler la question utilisateur pour optimiser le retrieval",
    "input": "{{user_query}}",
    "output": "{{optimized_query}}"
  },
  "module_2_retrieval": {
    "tool": "Pinecone/Supabase/Qdrant",
    "input": "{{optimized_query}}",
    "params": {"top_k": 5, "threshold": 0.7},
    "output": "{{retrieved_chunks}}"
  },
  "module_3_generation": {
    "model": "claude-sonnet-4-6",
    "prompt": "Pattern RAG Standard (voir ci-dessus)",
    "input": "{{retrieved_chunks}} + {{user_query}}",
    "output": "{{answer}}"
  }
}
```
