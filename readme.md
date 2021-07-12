@Paulo-Lopes-Estevao

``` Python
if __name__ == '__main__':
    
    msg= b"Mensagem para assinatura RSA"
    tess = criptsignature()
    tes =tess.signature(msg)
    
    msgg= b"Mensagem para assinatura RSA"
    v = tess.verify_signature(msgg,tes)
```
# teste de entrega