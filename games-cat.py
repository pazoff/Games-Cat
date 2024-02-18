from cat.mad_hatter.decorators import tool, hook, plugin
from cat.log import log

@hook
def agent_fast_reply(fast_reply, cat):
    return_direct = True
    
    # Get user message from the working memory
    message = cat.working_memory["user_message_json"]["text"]

    if message.startswith('@games'):
            
            games_available = """<b>GAMES CAT</b><br><br><img width="50%" src="https://raw.githubusercontent.com/pazoff/Games-Cat/main/games-cat.png">
                <br><b>Type:</b>
                <b>@trivia</b> - Challenge your knowledge with a variety of intriguing questions.
                <b>@cookie</b> - Delve into the sweet world of trivia challenges.
                <b>@puzzle</b> - Exercise your mind with captivating puzzles and brain teasers.
                <b>@tetris</b> - Experience the classic block-stacking game that never gets old.
                <b>@blackjack</b> - Blackjack + over 10 more games - Chess, Poker, Bridge, Roulette and more ...
                <b>@breakout</b> - Test your reflexes and skill in this timeless arcade favorite + 10 more games - Solitaire, Minesweeper, Snake, TikTakToe, Sudoku, Wordle and more ..."""

        
            return {"output": games_available}

    if message.startswith('@trivia'):
        
            return {"output": ' <iframe height="650" width="800" src="https://idev.games/appvert/game/1872/game54902/" title="Trivia"></iframe> '}
    
    if message.startswith('@cookie'):
        
            return {"output": ' <iframe height="650" width="800" src="https://www.smart-cookie-trivia.com/" title="Smart Cookie"></iframe> '}
    
    if message.startswith('@puzzle'):
        
            return {"output": ' <iframe height="650" width="800" src="https://html-classic.itch.zone/html/6586329/index.html" title="Puzzle"></iframe> '}
    
    if message.startswith('@tetris'):
        
            return {"output": ' <iframe height="650" width="800" src="https://idev.games/appvert/game/640/game30140/" title="Tetris"></iframe> '}
    
    if message.startswith('@breakout'):
        
            return {"output": ' <iframe height="650" width="500" src="https://www.lofiandgames.com/breakout" title="breakout"></iframe> '}
    
    if message.startswith('@blackjack'):
        
            return {"output": ' <iframe height="650" width="805" src="https://www.247blackjack.com/" title="blackjack"></iframe> '}

    return None
