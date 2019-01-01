import click,os
@click.command()
@click.option('--time1','-t1',help='the env of scripts')
@click.option('--time2','-t2',help='the env of scripts')
@click.option('--absolute','-a',default=os.getcwd(),help='xxx')
def main(time1,time2,absolute):
    print(time1)
    print(time2)
    print(absolute)

if __name__ == "__main__":
    main()