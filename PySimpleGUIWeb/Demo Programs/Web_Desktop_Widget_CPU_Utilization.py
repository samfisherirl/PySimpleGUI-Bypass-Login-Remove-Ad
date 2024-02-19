#!/usr/bin/env python
import PySimpleGUIWeb as sg
import psutil
import time
from threading import Thread
import operator


"""
    PSUTIL Desktop Widget
    Creates a floating CPU utilization window that is always on top of other windows
    You move it by grabbing anywhere on the window
    Good example of how to do a non-blocking, polling program using PySimpleGUI
    Use the spinner to adjust the number of seconds between readings of the CPU utilizaiton

    NOTE - you will get a warning message printed when you exit using exit button.
    It will look something like:
            invalid command name "1616802625480StopMove"
"""

# globale used to communicate with thread.. yea yea... it's working fine
g_interval = 1
g_cpu_percent = 0
g_procs = None
g_exit = False


def CPU_thread(args):
    global g_interval, g_cpu_percent, g_procs, g_exit

    while not g_exit:
        try:
            g_cpu_percent = psutil.cpu_percent(interval=g_interval)
            g_procs = psutil.process_iter()
        except:
            pass


def main():
    global g_interval,  g_procs, g_exit

    # ----------------  Create Form  ----------------
    sg.change_look_and_feel('Black')
    layout = [[sg.Text('', size=(8, 1), font=('Helvetica', 20), text_color=sg.YELLOWS[0],
                    justification='center', key='text')],
              [sg.Text('', size=(30, 8), font=('Courier New', 12),
                    text_color='white', justification='left', key='processes')],
              [sg.Exit(button_color=('white', 'firebrick4'),
                       pad=((15, 0), 0), size=(9, 1)), ]
              ]

    window = sg.Window('CPU Utilization', layout,
           no_titlebar=True, keep_on_top=True, alpha_channel=.8, grab_anywhere=True)

    # start cpu measurement thread
    thread = Thread(target=CPU_thread, args=(None,), daemon=True)
    thread.start()
    timeout_value = 1             # make first read really quick
    g_interval = 1
    # ----------------  main loop  ----------------
    while True:
        # --------- Read and update window --------
        event, values = window.read(
            timeout=timeout_value, timeout_key='Timeout')
        # --------- Do Button Operations --------
        if event in (None, 'Exit'):
            break

        timeout_value = 1000

        cpu_percent = g_cpu_percent
        display_string = ''
        if g_procs:
            # --------- Create list of top % CPU porocesses --------
            try:
                top = {proc.name(): proc.cpu_percent() for proc in g_procs}
            except:
                pass

            top_sorted = sorted(
                top.items(), key=operator.itemgetter(1), reverse=True)
            if top_sorted:
                top_sorted.pop(0)
            display_string = ''
            for proc, cpu in top_sorted:
                display_string += '{:2.2f} {}\n'.format(cpu/10, proc)

        # --------- Display timer and proceses in window --------
        window['text'].update('CPU {}'.format(cpu_percent))
        window['processes'].update(display_string)

    window.close()


if __name__ == "__main__":
    main()
