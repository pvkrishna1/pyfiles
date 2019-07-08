try:
    print("in try1")
    try:
        print("in try2")
    except(IndexError):
        print("in except 2")
    finally:
        print("in finally2")
except(ZeroDivisionError):
    print("in except1")
    try:
        print("in try3")
    except(KeyError):
        print("in except3")
    finally:
        print("in finally3")
finally:
    print("in finally 1")
    try:
        print("in try 4")
    except(ValueError):
        print("in except 4")
    finally:
        print("ni finally 4")

