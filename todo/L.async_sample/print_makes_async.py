#!/usr/bin/python3

from psycopg2 import connect
from psycopg2.extras import wait_select
from time import sleep

def wait_select_2(conn):
    """Wait until a connection or cursor has data available.

    The function is an example of a wait callback to be registered with
    `~psycopg2.extensions.set_wait_callback()`. This function uses
    :py:func:`~select.select()` to wait for data to become available, and
    therefore is able to handle/receive SIGINT/KeyboardInterrupt.
    """
    import select
    from psycopg2.extensions import POLL_OK, POLL_READ, POLL_WRITE

    while True:
        try:
            state = conn.poll()
            if state == POLL_OK:
                break
            elif state == POLL_READ:
                select.select([conn.fileno()], [], [])
            elif state == POLL_WRITE:
                select.select([], [conn.fileno()], [])
            else:
                raise conn.OperationalError(f"bad state from poll: {state}")
        except KeyboardInterrupt:
            conn.cancel()
            # the loop will be broken by a server error
            continue

def test_pg_async():
   aconn = connect(host="localhost", port=5433, user="postgres", password="1234", dbname="car_portal", async_=1)
   wait_select_2(aconn)

   acur = aconn.cursor()
   acur.execute("SELECT DISTINCT make FROM car_portal_app.car_model, "
             "pg_sleep(3)")

   for i in range(8):
       print("waiting... " + str(i))
       sleep(1)

   #wait_select_2(aconn)

   for row in acur:
       print(row[0])

   acur.close()
   aconn.close()

import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(host='localhost',
                                 port=5433,
                                 user='postgres',
                                 password="1234",
                                 database='car_portal')
    conn.add_log_listener(lambda conn, msg: print(msg))
    print("Executing a command")
    await conn.execute('''DO $$ BEGIN RAISE NOTICE 'Hello'; END; $$;''')
    print("Finished execution")
    await conn.close()

e = asyncio.get_event_loop()
e.run_until_complete(main())