from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'RUNNING'

@app.route('/<string:CPF>',methods=['GET'])
def home(CPF):
    is_blocked = False
    try:
        if not CPF.isdigit():
            return f"ERRO DE VALOR:: {CPF}\n Insira somente números",400
        
        num = "".join(filter(str.isdigit,CPF))

        if len(num) == 11:
            num = f"{num[:3]}.{num[3:6]}.{num[6:9]}-{num[9:11]}"
            with open("blacklist.txt") as f:
                for linha in f:
                    if linha.strip() == num:
                        is_blocked=True
                        break 
                    
        elif len(num) !=11:
            is_blocked = True
            return f'ERRO DE COMPRIMENTO:: {CPF} \n Não possui 11 caracteres', 400        
    

    
    except ValueError as e:
        print(f"\nError:: {e}\nConsulte o setor de T.I")

    if is_blocked:
        return 'BLOCKED',403
    
    else:
        return 'FREE',200


if __name__ == '__main__':
    app.run(debug = True)
    
