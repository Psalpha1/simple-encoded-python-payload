## simple-encoded-python-payload



# Features

- Contain a encode file that can make your own payload undetectable
- Simple and easy to edit script.
- Gain command prompt access.
- Multi-client support.

## How does work ?
   1. open ```server.py``` and set your IP_ADDRESS.
   
   2. open ```paylaod.txt``` and set set  IP_ADDRESS.
   
   3. run  ```server.py```.

```sh
python server.py
```
  
  4. run ```client.py``` (You can skip this step and compile the file using PYINSTALLER or PYARMOR).

```sh
python client.py
```

  5. Extra steps (If you just want to encode your own paylaod).
  make ```file.py``` import encode module & make this line of code.
    
```sh
print(encode.MASTER("""Your payload as <String Format>"""))
```
and then you can just decoded & run it with ```exec``` function.
