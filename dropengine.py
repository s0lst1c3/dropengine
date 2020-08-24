#!/usr/bin/env python

from core.dispatcher_cli import Dispatcher

if __name__ == '__main__':

    dispatcher = Dispatcher()

    dispatcher.parse_args()

    if dispatcher.options['master']['debug']:
        dispatcher.print_args()
        dispatcher.print_dispatch()

    interface = dispatcher.dispatch['interface']
    interface.initialize(dispatcher.dispatch, dispatcher.options)


    payload = interface.create_payload()

    if dispatcher.options['master']['output_file'] is not None:

        with open(dispatcher.options['master']['output_file'], 'w') as output_handle:
            output_handle.write(payload)

    else:

        print(payload)
