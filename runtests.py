if __name__ == "__main__":
    lim = 10
    num = input(f">> Please input test num you want to run from 0 to {10}: ")

    if not num.isdigit() or int(num) > lim if num.isdigit() else False:
        raise TypeError(f"Test number should be a number between 0 and {lim}")
    num = int(num)
    import os

    if num == 0:
        os.system("cat test_params_create | python console.py ")

    elif num == 1:
        import mytests.main_delete
