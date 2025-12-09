from pydantic import BaseModel, Field
from dataclasses import dataclass
from typing import List,Dict,Any,Optional

@dataclass
class PaperChunk(BaseModel):
    chunk_id: str
    paper_id: str
    text: str
    chunk_index: int
    section: str = "body"
def chunk_tool(text:str,paper_id:str,chunk_size : int = 1000,overlap: int = 200 ) -> List[PaperChunk]:
    """Chunk text with overlap"""
    paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 50]
        
    chunks = []
    current_chunk = ""
    chunk_idx = 0

    for para in paragraphs:
            if len(current_chunk) + len(para) > chunk_size and current_chunk:
                chunks.append(PaperChunk(
                    chunk_id=f"{paper_id}_chunk_{chunk_idx}",
                    paper_id=paper_id,
                    text=current_chunk.strip(),
                    chunk_index=chunk_idx
                ))

                 # Add overlap from previous chunk
                sentences = current_chunk.split('. ')
                overlap_text = '. '.join(sentences[-2:]) if len(sentences) > 2 else ""
                current_chunk = overlap_text + "\n\n" + para
                chunk_idx += 1
            else:
                current_chunk += "\n\n" + para
     
        
    # Add final chunk
    if current_chunk:
        chunks.append(PaperChunk(
            chunk_id=f"{paper_id}_chunk_{chunk_idx}",
            paper_id=paper_id,
            text=current_chunk.strip(),
            chunk_index=chunk_idx
        ))
    
    return chunks
    
    