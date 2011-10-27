.. _Scheduler:


.. currentmodule:: pyev


===========================================
:py:class:`Scheduler` --- Scheduler watcher
===========================================


.. py:class:: Scheduler(scheduler, loop, callback[, data=None, priority=0])

    :param callable scheduler: reschedule callback. See :py:attr:`scheduler`.

    :type loop: :py:class:`Loop`
    :param loop: loop object responsible for this watcher (accessible through
        :py:attr:`Watcher.loop`).

    :param callable callback: See :py:attr:`Watcher.callback`.

    :param object data: any Python object you might want to attach to the
        watcher (stored in :py:attr:`Watcher.data`).

    :param int priority: See :py:attr:`Watcher.priority`.

    :py:class:`Scheduler` watchers are specialised :py:class:`Periodic` watchers.
    Each time the :py:class:`Scheduler` gets scheduled, the reshedule callback
    (:py:attr:`scheduler`) will be called with the watcher as first, and the
    current time as second argument. Example::

        def myscheduler(watcher, now):
            return now + 60.0

        Scheduler(myscheduler, ...)

    This can be used to create very complex timers, such as a timer that
    triggers on 'next midnight, local time'. To do this, you would calculate the
    next midnight after *now* and return the timestamp value for this. This
    cannot be done with :py:class:`Timer` watchers, as those cannot react to
    time jumps.

    .. seealso::
        `ev_periodic - to cron or not to cron?
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_periodic_code_to_cron_or_not>`_


    .. py:method:: reset

        Simply stops and restarts the periodic watcher again. This is only
        useful when :py:attr:`scheduler` would return a different time than the
        last time it was called (e.g. in a crond like program when the crontabs
        have changed).


    .. py:method:: at() -> float

        When the watcher is active, returns the absolute time that this watcher
        is supposed to trigger next.


    .. py:attribute:: scheduler

        The current reschedule callback. Can be changed any time.

        Its signature must be:

        .. py:method:: scheduler(watcher, now) -> float
            :noindex:

            :type watcher: :py:class:`Scheduler`
            :param watcher: this watcher.

            :param float now: the current time.

        It must return a :py:class:`float` greater than or equal to the *now*
        argument to indicate the next time the watcher callback should be
        scheduled. It will usually be called just before the callback will be
        triggered, but might be called at other times, too.

        .. warning::
            * This callback **must not** stop or destroy any watcher, ever, or
              make **any** other event loop modifications whatsoever. If you
              need to stop it, return ``now + 1e+30`` and stop it afterwards
              (e.g. by starting a :py:class:`Prepare` watcher, which is the only
              event loop modification you are allowed to do).
            * If the reshedule callback raises an error, or returns anything but
              a :py:class:`float`, pyev will stop this watcher.
