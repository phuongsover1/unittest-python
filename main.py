def do_stuff(num=0):
    try:
        return int(num) + 5
    except TypeError as err:
        return err
    except ValueError as err:
        return err
