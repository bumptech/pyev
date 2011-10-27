.. _Watcher:


.. currentmodule:: pyev


========
Watchers
========


.. toctree::
    :maxdepth: 1

    Io
    Timer
    Periodic
    Scheduler
    Signal
    Child
    Stat
    Idle
    Prepare_Check
    Embed
    Fork
    Async




Common methods and attributes
=============================

:py:class:`Watcher` is the base class for all watchers. Though it is not exposed
to users, its methods and attributes are described here.

.. py:class:: Watcher

    .. seealso::
        `ANATOMY OF A WATCHER
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#ANATOMY_OF_A_WATCHER>`_


    .. py:method:: start

        Starts (activates) the watcher. Only active watchers will receive
        events. If the watcher is already active nothing will happen.


    .. py:method:: stop

        Stops the watcher if active, and clears the pending status (whether the
        watcher was active or not).

        It is possible that stopped watchers are pending - for example,
        non-repeating timers are being stopped when they become pending - but
        :py:meth:`stop` ensures that the watcher is neither active nor pending.



    .. py:method:: invoke(revents)

        :param int revents: See :ref:`Watcher_revents` for valid values.

        Invoke the watcher callback with the given *revents*.


    .. py:method:: clear() -> int

        If the watcher is pending, this method clears its pending status and
        returns its *revents* bitset (as if its callback was invoked). If the
        watcher isn't pending it does nothing and returns ``0``.

        Sometimes it can be useful to 'poll' a watcher instead of waiting for
        its callback to be invoked, which can be accomplished with this function.



    .. py:method:: feed(revents)

        :param int revents: See :ref:`Watcher_revents` for valid values.

        Feeds the given *revents* set into the event loop, as if the specified
        event had happened for the watcher.


    .. py:attribute:: active

        *Read only*

        :py:const:`True` if the watcher is active (i.e. it has been started and
        not yet been stopped), :py:const:`False` otherwise.

        As long as a watcher is active you must not modify it.


    .. py:attribute:: pending

        *Read only*

        :py:const:`True` if the watcher is pending, (i.e. it has outstanding
        events but its callback has not yet been invoked), :py:const:`False`
        otherwise.

        As long as a watcher is pending (but not active) you must not change its
        priority.


    .. py:attribute:: loop

        *Read only*

        :py:class:`Loop` object responsible for the watcher.


    .. py:attribute:: callback

        The current watcher callback, its signature must be:

        .. py:method:: callback(watcher, revents)
            :noindex:

            :type watcher: a subclass of :py:class:`Watcher`
            :param watcher: this watcher.

            :param int revents: See :ref:`Watcher_revents` for valid values.

        As a rule you should not let the callback return with unhandled
        exceptions. The loop 'does not know' what to do with an exception
        happening in your callback (it depends largely on what **you** are
        doing), so, by default, it will just print a warning and suppress it.
        This behaviour can be changed by setting :py:attr:`Loop.debug` to
        :py:const:`True`, in which case pyev will stop the loop on all errors.
        If you want to act on an exception, you're better off doing it in the
        callback (where you are allowed to do anything needed, like logging,
        stopping/restarting the loop, etc.). Example::

            def mycallback(watcher, revents):
                try:
                    pass #do something interesting
                except Exception:
                    logging.exception("FATAL!") #this will also log the traceback
                    watcher.stop() #stop the watcher
                    watcher.loop.stop() #stop the loop

        If you have a lot of callbacks, use decorators::

            def mydecorator(func):
                def wrap(watcher, revents):
                    try:
                        func(watcher, revents)
                    except RuntimeError: #these are not fatal
                        logging.exception("stopping {0}".format(watcher))
                        watcher.stop() #stop the watcher but let the loop continue its merry way
                    except Exception: #all other exceptions are fatal
                        logging.exception("FATAL: stopping {0} and {1}".format(watcher, watcher.loop))
                        watcher.stop() #stop the watcher
                        watcher.loop.stop() #stop the loop
                return wrap

            @mydecorator
            def mycallback(watcher, revents):
                pass #do something interesting


    .. py:attribute:: data

        watcher data.


    .. py:attribute:: priority

        Set and query the priority of the watcher. The priority is a small
        integer between :py:const:`EV_MAXPRI` and :py:const:`EV_MINPRI`. Pending
        watchers with higher priority will be invoked before watchers with lower
        priority, but priority will not keep watchers from being executed
        (except for :py:class:`Idle` watchers).
        If you need to suppress invocation when higher priority events are
        pending you need to look at :py:class:`Idle` watchers, which provide
        this functionality.

        Setting a priority outside the range of :py:const:`EV_MINPRI` to
        :py:const:`EV_MAXPRI` is fine, as long as you do not mind that the
        priority value you query might or might not have been clamped to the
        valid range (see also :ref:`Watcher_priorities`).

        The default priority used by watchers when no priority has been set is
        always ``0``.

        You must not change the priority of a watcher as long as it is active or
        pending.

        .. seealso::
            `WATCHER PRIORITY MODELS
            <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#WATCHER_PRIORITY_MODELS>`_


.. _Watcher_revents:

Watcher received events
=======================

.. py:data:: EV_IO

.. py:data:: EV_READ

    The file descriptor in the :py:class:`Io` watcher has become readable.

.. py:data:: EV_WRITE

    The file descriptor in the :py:class:`Io` watcher has become writable.

.. py:data:: EV_TIMER

    The :py:class:`Timer` watcher has timed out.

.. py:data:: EV_PERIODIC

    The :py:class:`Periodic` watcher has timed out.

.. py:data:: EV_SIGNAL

    The signal specified in the :py:class:`Signal` watcher has been received by
    a thread.

.. py:data:: EV_CHILD

    The pid specified in the :py:class:`Child` watcher has received a status
    change.

.. py:data:: EV_STAT

    The path specified in the :py:class:`Stat` watcher changed its attributes
    somehow.

.. py:data:: EV_IDLE

    The :py:class:`Idle` watcher has determined that you have nothing better to
    do.

.. py:data:: EV_PREPARE

.. py:data:: EV_CHECK

    All :py:class:`Prepare` watchers are invoked just before
    :py:meth:`Loop.start` starts to gather new events, and all :py:class:`Check`
    watchers are invoked just after :py:meth:`Loop.start` has gathered them, but
    before it invokes any callbacks for any received events. Callbacks of both
    watcher types can start and stop as many watchers as they want, and all of
    them will be taken into account (for example, a :py:class:`Prepare` watcher
    might start an :py:class:`Idle` watcher to keep :py:meth:`Loop.start` from
    blocking).

.. py:data:: EV_EMBED

    The embedded event loop specified in the :py:class:`Embed` watcher needs
    attention.

.. py:data:: EV_FORK

    The event loop has been resumed in the child process after fork (see
    :py:class:`Fork`).

.. py:data:: EV_ASYNC

    The given :py:class:`Async` watcher has been asynchronously notified.

.. py:data:: EV_CUSTOM

    Not ever sent (or otherwise used) by libev itself, but can be freely used by
    users to signal watchers (e.g. via :py:meth:`Watcher.feed`).

.. py:data:: EV_ERROR

    An unspecified error has occurred, the watcher has been stopped. This might
    happen because the watcher could not be properly started because libev ran
    out of memory, a file descriptor was found to be closed or any other problem.
    libev considers these application bugs.

    .. warning::
        pyev handle this event as a fatal error. On receiving this event pyev
        will **stop the loop** (and the watcher). The callback will **not** be
        invoked. In practice users should never receive this event (still
        present for testing purposes).


.. _Watcher_priorities:

Watcher priorities
==================

Unfortunately the range of valid priorities is defined at compile time. If you
really need to change it you can still define new values in setup.py and rebuild
pyev, example::

    setup(
          ...,
          ext_modules=[
                       Extension("pyev",
                                 ["src/pyev.c"],
                                 define_macros=[
                                                # uncomment the following
                                                # to modify priorities
                                                ("EV_MINPRI", "-5"),
                                                ("EV_MAXPRI", "5"),
                                               ]
                                ),
                      ],
          ...
         )

.. py:data:: EV_MINPRI

    default: ``-2``.

.. py:data:: EV_MAXPRI

    default: ``2``.
