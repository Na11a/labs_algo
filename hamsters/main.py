from model import Hamster
if __name__=="__main__":
    result = Hamster.can_buy('hamsters_in.txt')
    print(result)
    output = open('output.txt','w').writelines(f'result = {result}')