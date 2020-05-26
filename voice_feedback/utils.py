from IPython.display import display, clear_output
import os

def two_buttons(yes, no, callback):
    from ipywidgets import Button

    yes_btn = Button(description=yes)
    no_btn = Button(description=no)

    yes_btn.on_click(lambda _: callback(True))
    no_btn.on_click(lambda _: callback(False))

    display(yes_btn)
    display(no_btn)


def iter_sequence(it, fn):
    it = iter(it)
    clear_output()

    try:
        item = next(it)
        fn(item, lambda: iter_sequence(it, fn))
    except StopIteration:
        print('Done.')
        pass

def new_item_path(base_path, label):
    ds_dir = f'{base_path}/{label}'
    n = len(os.listdir(ds_dir))
    return f'{ds_dir}/{n:05d}.wav'
