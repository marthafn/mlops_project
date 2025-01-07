import typer

def greeting(count: int,msg:str):
    for j in range(count):
        print(msg)
        
typer.run(greeting)
