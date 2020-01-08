import sys

def print_status(zankin,otsuri,p_name = "-",d_stastus = "-",d_zankin = "-"):
  print("%s %s %s %s %s" % (str(zankin),str(otsuri),p_name,str(d_stastus),str(d_zankin)))

def check(coin10,coin50,coin100,coin500,price):
  total_coin = coin10 * 10 + coin50 * 50 + coin100 * 100 + coin500 * 500
  if total_coin >= price:
    return True
  else:
    return False

def main(lines):
    zankin = 0
    otsuri = 0
    b, n = map(int,lines[0].split())
    coin10,coin50,coin100,coin500 = map(int,lines[1].split())
    stock = []
    for i in range(b):
      stock.append(lines[i+2].split())
    for i in range(n):
      input_cmd = lines[2+b+i].split()
      if input_cmd[0] == "+":
        zankin += int(input_cmd[1])
        print_status(zankin,otsuri)

      elif input_cmd[0] == "*":
        for j in stock:
          if j[0] == input_cmd[1] and int(j[2]) >= 1 and check(coin10,coin50,coin100,coin500,int(j[1])) == True and zankin >= int(j[1]):
            zankin -= int(j[1])
            j[2] = str(int(j[2]) - 1)
      elif input_cmd[0] == "#":
        otsuri = zankin
        zankin = 0
        print_status(zankin,otsuri)

if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
