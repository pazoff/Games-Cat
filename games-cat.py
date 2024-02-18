from cat.mad_hatter.decorators import tool, hook, plugin
from cat.log import log

@hook
def agent_fast_reply(fast_reply, cat):
    return_direct = True
    
    # Get user message from the working memory
    message = cat.working_memory["user_message_json"]["text"]

    if message.startswith('@games'):
        
            return {"output": 'Type: @trivia or @cookie or @puzzle or @tetris'}

    if message.startswith('@trivia'):
        
            return {"output": ' <iframe height="650" width="800" src="https://idev.games/appvert/game/1872/game54902/" title="Trivia"></iframe> '}
    
    if message.startswith('@cookie'):
        
            return {"output": ' <iframe height="650" width="800" src="https://www.smart-cookie-trivia.com/" title="Smart Cookie"></iframe> '}
    
    if message.startswith('@puzzle'):
        
            return {"output": ' <iframe height="650" width="800" src="https://html-classic.itch.zone/html/6586329/index.html" title="Puzzle"></iframe> '}
    
    if message.startswith('@tetris'):
        
            return {"output": ' <iframe height="650" width="800" src="https://idev.games/appvert/game/640/game30140/" title="Tetris"></iframe> '}

    return None
