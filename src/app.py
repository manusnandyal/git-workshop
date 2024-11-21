git clone https://huggingface.co/spaces/manusnandyal/blabla1

import gradio as gr
from transformers import pipeline

class Hit(TypedDict):
  cid: str
  score: float
  text: str

## YOUR_CODE_STARTS_HERE
def querying(query: str) -> List[Hit]:
  ranking = bm25_retriever.retrieve(query=query)
  results = []
  data = sciq.corpus
  for cid, score in ranking.items():
    for doc in data:
      if doc.collection_id == cid:
        results.append(Hit(cid=cid, score=score, text=doc.text))
      else:
        results.append(Hit(cid=cid, score=score, text=""))
  return results

## YOUR_CODE_ENDS_HERE

demo: Optional[gr.Interface] = gr.Interface(fn=querying,inputs=gr.Textbox(),outputs=gr.Textbox()
)  # Assign your gradio demo to this variable
return_type = List[Hit]
demo.launch()
