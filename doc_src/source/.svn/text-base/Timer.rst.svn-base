.. _Timer:


.. currentmodule:: pyev


===================================
:py:class:`Timer` --- Timer watcher
===================================


.. py:class:: Timer(after, repeat, loop, callback[, data=None, priority=0])

    :param float after: configure the timer to trigger after *after* seconds.

    :param float repeat: If repeat is ``0.0``, then it will automatically be
        stopped once the timeout is reached. If it is positive, then the
        timer will automatically be configured to trigger again every
        *repeat* seconds later, until stopped manually.

    :type loop: :py:class:`Loop`
    :param loop: loop object responsible for this watcher (accessible through
        :py:attr:`Watcher.loop`).

    :param callable callback: See :py:attr:`Watcher.callback`.

    :param object data: any Python object you might want to attach to the
        watcher (stored in :py:attr:`Watcher.data`).

    :param int priority: See :py:attr:`Watcher.priority`.

    :py:class:`Timer` watchers are simple relative timers that generate an event
    after a given time, and optionally repeating in regular intervals after that.

    The timers are based on real time, that is, if you register an event that
    times out after an hour and you reset your system clock to January last
    year, it will still time out after (roughly) one hour. 'Roughly' because
    detecting time jumps is hard, and some inaccuracies are unavoidable.

    The callback is guaranteed to be invoked only after its timeout has passed
    (not *at*, so on systems with very low-resolution clocks this might
    introduce a small delay). If multiple timers become ready during the same
    loop iteration then the ones with earlier time-out values are invoked before
    ones of the same priority with later time-out values (but this is no longer
    true when a callback calls :py:meth:`Loop.start` recursively).

    The timer itself will do a best-effort at avoiding drift, that is, if you
    configure a timer to trigger every ``10`` seconds, then it will normally
    trigger at exactly ``10`` second intervals. If, however, your program cannot
    keep up with the timer (because it takes longer than those ``10`` seconds to
    do stuff) the timer will not fire more than once per event loop iteration.

    .. seealso::
        `ev_timer - relative and optionally repeating timeouts
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_timer_code_relative_and_opti>`_

            * `Be smart about timeouts
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Be_smart_about_timeouts>`_
            * `The special problem of time updates
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#The_special_problem_of_time_updates>`_
            * `The special problems of suspended animation
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#The_special_problems_of_suspended_an>`_


    .. py:method:: set(after, repeat)

        :param float after: configure the timer to trigger after *after* seconds.

        :param float repeat: If repeat is ``0.0``, then it will automatically be
            stopped once the timeout is reached. If it is positive, then the
            timer will automatically be configured to trigger again every
            *repeat* seconds later, until stopped manually.

        Configures the watcher.


    .. py:method:: reset

        This will act as if the timer timed out and restart it again if it is
        repeating. The exact semantics are:

        * if the timer is pending, its pending status is cleared.
        * if the timer is started but non-repeating, stop it (as if it timed out).
        * if the timer is repeating, either start it if necessary (with the
          :py:attr:`repeat` value), or reset the running timer to the
          :py:attr:`repeat` value.

        .. seealso::
            `Be smart about timeouts
            <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Be_smart_about_timeouts>`_,
            for a usage example.


    .. py:method:: remaining() -> float

        Returns the remaining time until a timer fires. If the timer is active,
        then this time is relative to the current event loop time, otherwise
        it's the timeout value currently configured.

        That is, after instanciating a :py:class:`Timer` with an *after* value
        of ``5.0`` and a *repeat* value of ``7.0``, :py:meth:`remaining` returns
        ``5.0``. When the timer is started and one second passes,
        :py:meth:`remaining` will return ``4.0``. When the timer expires and is
        restarted, it will return roughly ``7.0`` (likely slightly less as
        callback invocation takes some time, too), and so on.


    .. py:attribute:: repeat

        The current *repeat* value. Will be used each time the watcher times out
        or :py:meth:`reset` is called, and determines the next timeout (if any),
        which is also when any modifications are taken into account.
