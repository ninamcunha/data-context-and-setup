import os
import pandas as pd
import os.path

class Olist:
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """
        csv_path = __file__.replace("/olist/data.py", "/data/csv/")

        file_names=os.listdir(csv_path)
        for file in file_names:
            if file.endswith('.csv')!=True:
                file_names.remove(file)

        key_names = file_names.copy()
        for i in range(len(key_names)):
            key_names[i] = key_names[i].replace('_dataset.csv', '')
            key_names[i] = key_names[i].replace('.csv', '')
            key_names[i] = key_names[i].replace('olist_', '')

        data = {}
        for i, file in enumerate(file_names):
            data[key_names[i]] = pd.read_csv(os.path.join(csv_path, file))

        # Hints 1: Build csv_path as "absolute path" in order to call this method from anywhere.
            # Do not hardcode your path as it only works on your machine ('Users/username/code...')
            # Use __file__ instead as an absolute path anchor independant of your usename
            # Make extensive use of `breakpoint()` to investigate what `__file__` variable is really
        # Hint 2: Use os.path library to construct path independent of Mac vs. Unix vs. Windows specificities
        return data

    def ping(self):
        """
        You call ping I print pong.
        """
        print("pong")
