#!/bin/bash

# Tester l'endpoint /chat avec un exemple de prompt
curl -X POST http://localhost:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"prompt": "What is a LLM?"}'
