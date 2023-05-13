# List2Random
CLI Tool that allows the user to input a list, then the script randomly picks between the entered options.
## Requeriments

- Python 3
- argparse ```pip install argparse ```


## Arguments
| Argument | Description |
| ------ | ------ |
| -l --list | List of elements separated by commas. If the element has blank spaces you must use quotes. Default: Numbers from one to ten. |
| -a --amount | Amount of elements that the user wants to be randomly picked. Default: 1. |


## Using the script

### Default mode
```sh
cd List2Random
python .\List2Random.py 
```
The result will be a random number from 1 to 10.
### Normal use
```sh
cd List2Random
python .\List2Random.py -a 3 -l "Darling in the FranXX","Oshi no Ko",Toradora,Dororo,"Psycho Pass"
```
The result will be a list of 3 random elements. In this case for example: 1. Toradora 2. Oshi no Ko 3. Darling in the FranXX