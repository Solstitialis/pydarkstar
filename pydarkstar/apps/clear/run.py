# -*- coding: utf-8 -*-
"""
Clear the auction house.
"""
import logging

from .options import Options

from ... import logutils
from ...database import Database
from ...auction.manager import Manager


def main():
    """
    Main function.
    """
    # get options
    opts = Options()
    logutils.basic_config(verbose=opts.verbose, silent=opts.silent, fname='pydarkstar.log')
    opts.log_values(level=logging.INFO)

    # create auction house manager
    manager = Manager.create_database_and_manager(
        hostname=opts.hostname,
        database=opts.database,
        username=opts.username,
        password=opts.password,
        name=opts.name,
        fail=opts.fail
    )

    # clear all items
    if opts.all:
        # really?
        if not opts.force:
            raise RuntimeError('clearing all items from auction house is dangerous. use --force')
        else:
            manager.cleaner.clear(seller=None)
    # clear seller items
    else:
        if not opts.force:
            raise RuntimeError('clearing all items from auction house is dangerous. use --force')
        else:
            manager.cleaner.clear(seller=manager.seller.seller)

    # exit after clearing
    logging.info('exit after clear')
    return


def cleanup():
    logging.info('exit\n')


if __name__ == '__main__':
    with logutils.capture():
        main()
    cleanup()