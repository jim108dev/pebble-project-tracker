#!/usr/bin/env python

"""
 Read feedback from a csv file. Integrate it in the current findings. Delete the file.
"""

import os
import os.path
import shutil
import tempfile
from datetime import datetime

import pandas as pd

from util import get_conf

OUTPUT_COLUMNS = ["id", "v1","v2","v3","v4", "date"]


def main(conf):
    if not os.path.isfile(conf.feedback_filename):
        print("%s does not exist" % conf.feedback_filename)
        return

    feedback_df = pd.read_csv(conf.feedback_filename, sep=';')
    log_df = pd.read_csv(conf.log_filename, sep=';')

    df = pd.concat([log_df, feedback_df])

    df.to_csv(path_or_buf=conf.log_filename,
              columns=OUTPUT_COLUMNS, index=False, sep=";", mode='a', header=False)

    os.remove(conf.feedback_filename)

if __name__ == "__main__":
    main(get_conf())
