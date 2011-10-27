.. _Loop:


.. currentmodule:: pyev


===============================
:py:class:`Loop` --- Event loop
===============================


.. py:class:: Loop([flags=EVFLAG_AUTO, callback=None, data=None, debug=False, io_interval=0.0, timeout_interval=0.0])

    :param int flags: can be used to specify special behaviour or specific
        backends to use. See :ref:`Loop_flags` for more details.

    :type callback: callable or None
    :param callback: If omitted or :py:const:`None` the loop will fall back to
        its default behaviour of calling :c:func:`ev_invoke_pending` when
        required.
        If it is a :py:class:`callable`, then the loop will execute it instead
        and it becomes the user's responsibility to call :py:meth:`invoke`
        to invoke pending events. See also :py:attr:`callback`.

    :param object data: any Python object you might want to attach to the loop
        (will be stored in :py:attr:`data`).

    :param bool debug: See :py:attr:`debug`.

    :param float io_interval: See :py:attr:`io_interval`.

    :param float timeout_interval: See :py:attr:`timeout_interval`.

    Instanciates a new event loop that is always distinct from
    the *default loop*. Unlike the *default loop*, it cannot handle
    :py:class:`Child` watchers, and attempts to do so will raise an
    :py:exc:`Error`.

    One common way to use libev with threads is indeed to create one
    :py:class:`Loop` per thread, and use the *default loop* (from
    :py:func:`default_loop`) in the 'main' or 'initial' thread

    .. seealso::
        `FUNCTIONS CONTROLLING EVENT LOOPS
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#FUNCTIONS_CONTROLLING_EVENT_LOOPS>`_


    .. py:method:: start([flags])

        :param int flags: defaults to ``0``. See :ref:`Loop_start_flags`.

        This method usually is called after you have initialised all your
        watchers and you want to start handling events.


    .. py:method:: stop([how])

        :param int how: defaults to :py:const:`EVBREAK_ONE`.
            See :ref:`Loop_stop_how`.

        Can be used to make a call to :py:meth:`start` return early (but only
        after it has processed all outstanding events).


    .. py:method:: invoke

        This method will simply invoke all pending watchers while resetting
        their pending state. Normally, the loop does this automatically when
        required, but when setting the :py:attr:`callback` attribute this
        call comes in handy.


    .. py:method:: reset

        This method sets a flag that causes subsequent loop iterations to
        reinitialise the kernel state for backends that have one. You can call
        it anytime, but it makes most sense after forking, in the child process.
        You **must** call it (or use :py:const:`EVFLAG_FORKCHECK`) in the child
        before calling :py:meth:`resume` or :py:meth:`start`. Again, you have to
        call it on any loop that you want to re-use after a fork, even if you do
        not plan to use the loop in the parent.

        On the other hand, you only need to call this method in the child
        process if and only if you want to use the event loop in the child. If
        you just :c:func:`fork`\ +\ :c:func:`exec` or create a new loop in the
        child, you don't have to call it at all.


    .. py:method:: now() -> float

        Returns the current 'event loop time', which is the time the event loop
        received events and started processing them. This timestamp does not
        change as long as callbacks are being processed, and this is also the
        base time used for relative timers. You can treat it as the timestamp of
        the event occurring (or more correctly, libev finding out about it).


    .. py:method:: update

        Establishes the current time by querying the kernel, updating the time
        returned by :py:meth:`now` in the progress. This is a costly
        operation and is usually done automatically within the loop.
        This method is rarely useful, but when some event callback runs for a
        very long time without entering the event loop, updating libev's idea
        of the current time is a good idea.

        .. seealso::
            `The special problem of time updates
            <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#The_special_problem_of_time_updates>`_


    .. py:method:: suspend

    .. py:method:: resume

        These two methods should be used when the loop is not used for a while
        and timeouts should not be processed.
        A typical use case would be an interactive program such as a game: when
        the user presses :kbd:`Control-z` to suspend the game and resumes it an
        hour later it would be best to handle timeouts as if no time had
        actually passed while the program was suspended. This can be achieved by
        calling :py:meth:`suspend` in your :c:data:`SIGTSTP` handler, sending
        yourself a :c:data:`SIGSTOP` and calling :py:meth:`resume` directly
        afterwards to resume timer processing.

        Effectively, all :py:class:`Timer` watchers will be delayed by the time
        spent between :py:meth:`suspend` and :py:meth:`resume`, and all
        :py:class:`Periodic` watchers will be rescheduled (that is, they will
        lose any events that would have occurred while suspended).
        After calling :py:meth:`suspend` you must not call any method on the
        loop other than :py:meth:`resume`, and you must not call
        :py:meth:`resume` without a previous call to :py:meth:`suspend`.
        Calling :py:meth:`suspend`\ /\ :py:meth:`resume` has the side effect of
        updating the event loop time (see :py:meth:`update`).


    .. py:method:: unref

    .. py:method:: ref

        :py:meth:`unref`\ /\ :py:meth:`ref` can be used to add or remove a
        reference count on the event loop: every watcher keeps one reference,
        and as long as the reference count is nonzero, the loop will not return
        on its own.

        This is useful when you have a watcher that you never intend to
        unregister, but that nevertheless should not keep the loop from
        returning. In such a case, call :py:meth:`unref` after starting, and
        :py:meth:`ref` before stopping it.
        As an example, libev itself uses this for its internal signal pipe: it
        is not visible to the user and should not keep the loop from exiting if
        no event watchers registered by it are active. It is also good to do
        this for generic recurring timers or from within third-party libraries.
        Just remember to :py:meth:`unref` after :py:meth:`Watcher.start` and
        :py:meth:`ref` before :py:meth:`Watcher.stop` (but only if the watcher
        wasn't active before, or was active before, respectively. Note also that
        libev might stop watchers itself (e.g. non-repeating timers) in which
        case you have to :py:meth:`ref` in the callback).

        .. note::
             These two methods have nothing to do with Python reference counting.


    .. py:method:: verify

        This method only does something with a debug build of pyev (which needs
        a debug build of Python). It tries to go through all internal structures
        and checks them for validity. If anything is found to be inconsistent,
        it will print an error message to standard error and call :c:func:`abort`.
        This can be used to catch bugs inside libev itself: under normal
        circumstances, this method should never abort.


    .. py:attribute:: backend

        *Read only*

        One of the :ref:`Loop_backends` flags indicating the event backend in
        use.


    .. py:attribute:: default

        *Read only*

        :py:const:`True` if the loop is the *default loop*, :py:const:`False`
        otherwise.


    .. py:attribute:: depth

        *Read only*

        The number of times :py:meth:`start` was entered minus the number of
        times :py:meth:`start` was exited normally, in other words, the
        recursion depth. Outside :py:meth:`start`, this number is ``0``. In a
        callback, this number is ``1``, unless :py:meth:`start` was invoked
        recursively (or from another thread), in which case it is higher.


    .. py:attribute:: iteration

        *Read only*

        The current iteration count for the loop, which is identical to the
        number of times libev did poll for new events. It starts at ``0`` and
        happily wraps around with enough iterations. This value can sometimes be
        useful as a generation counter of sorts (it 'ticks' the number of loop
        iterations), as it roughly corresponds with :py:class:`Prepare` and
        :py:class:`Check` calls - and is incremented between the prepare and
        check phases.


    .. py:attribute:: pending

        *Read only*

        The number of pending watchers - ``0`` indicates that no watchers are
        pending.


    .. py:attribute:: callback

        The current invoke pending callback, its signature must be:

        .. py:method:: callback(loop)
            :noindex:

            :type loop: :py:class:`Loop` object
            :param loop: this loop.

        This overrides the invoke pending functionality of the loop: instead of
        invoking all pending watchers when there are any, the loop will call
        this callback instead (use :py:meth:`invoke` if you want to invoke all
        pending watchers). This is useful, for example, when you want to invoke
        the actual watchers inside another context (another thread, etc.).

        If you want to reset the callback, set it to :py:const:`None`.

        .. warning::
             If the callback raises an error, pyev will **stop the loop**.


    .. py:attribute:: data

        loop data.


    .. py:attribute:: debug

        This affects the behaviour of the loop while executing all watcher
        callbacks (:py:attr:`Watcher.callback` and :py:attr:`Periodic.scheduler`).

        If :py:const:`False` (the default), when a callback returns with an
        unhandled exception, the loop will print a warning and suppress the
        exception, in this configuration, the loop will **only stop on fatal
        errors** (memory allocation failure, :py:const:`EV_ERROR` received, ...).

        If :py:const:`True`, the loop will **stop on all errors** (you do not
        want that if you write a server).


    .. py:attribute:: io_interval

    .. py:attribute:: timeout_interval

        These two attributes influence the time that libev will spend waiting
        for events. Both time intervals are by default ``0.0``, meaning that
        libev will try to invoke :py:class:`Timer`\ /\ :py:class:`Periodic`
        callbacks and :py:class:`Io` callbacks with minimum latency.
        Setting these to a higher value (the interval must be >= ``0``) allows
        libev to delay invocation of :py:class:`Io` and :py:class:`Timer`\ /\
        :py:class:`Periodic` callbacks to increase efficiency of loop iterations
        (or to increase power-saving opportunities).
        The idea is that sometimes your program runs just fast enough to handle
        one (or very few) event(s) per loop iteration. While this makes the
        program responsive, it also wastes a lot of CPU time to poll for new
        events, especially with backends like ``select`` which have a high
        overhead for the actual polling but can deliver many events at once.

        By setting a higher *io_interval* you allow libev to spend more time
        collecting :py:class:`Io` events, so you can handle more events per
        iteration, at the cost of increasing latency. Timeouts (both
        :py:class:`Periodic` and :py:class:`Timer`) will not be affected.
        Setting this to a non-zero value will introduce an additional
        :py:func:`sleep` call into most loop iterations. The sleep time ensures
        that libev will not poll for :py:class:`Io` events events more often
        than once per this interval, on average.
        Many (busy) programs can usually benefit by setting the *io_interval* to
        a value near ``0.1`` or so, which is often enough for interactive
        servers (of course not for games), likewise for timeouts. It usually
        doesn't make much sense to set it to a lower value than ``0.01``, as
        this approaches the timing granularity of most systems. Note that if you
        do transactions with the outside world and you can't increase the
        parallelism, then this setting will limit your transaction rate (if you
        need to poll once per transaction and the *io_interval* is ``0.01``,
        then you can't do more than ``100`` transactions per second).

        Likewise, by setting a higher *timeout_interval* you allow libev to
        spend more time collecting timeouts, at the expense of increased
        latency/jitter/inexactness (the watcher callback will be called later).
        :py:class:`Io` watchers will not be affected.
        Setting this to a non-zero value will not introduce any overhead in libev.
        Setting the *timeout_interval* can improve the opportunity for saving
        power, as the program will 'bundle' timer callback invocations that are
        'near' in time together, by delaying some, thus reducing the number of
        times the process sleeps and wakes up again. Another useful technique to
        reduce iterations/wake-ups is to use :py:class:`Periodic` watchers and
        make sure they fire on, say, one-second boundaries only.


.. _Loop_flags:

:py:class:`Loop` *flags*
========================

behaviour
---------

.. py:data:: EVFLAG_AUTO

    The default *flags* value.

.. py:data:: EVFLAG_NOENV

    If this flag bit is or'ed into the *flags* value (or the program runs
    :c:func:`setuid` or :c:func:`setgid`) then libev will not look at the
    environment variable :envvar:`LIBEV_FLAGS`. Otherwise (the default),
    :envvar:`LIBEV_FLAGS` will override the *flags* completely if it is found in
    the environment. This is useful to try out specific backends to test their
    performance, or to work around bugs.

.. py:data:: EVFLAG_FORKCHECK

    Instead of calling :py:meth:`Loop.reset` manually after a fork, you can also
    make libev check for a fork in each iteration by enabling this flag.
    This works by calling :c:func:`getpid` on every iteration of the loop, and
    thus this might slow down your event loop if you do a lot of loop iterations
    and little real work, but is usually not noticeable.
    The big advantage of this flag is that you can forget about fork (and forget
    about forgetting to tell libev about forking) when you use it.
    This flag setting cannot be overridden or specified in the
    :envvar:`LIBEV_FLAGS` environment variable.

.. py:data:: EVFLAG_NOINOTIFY

    When this flag is specified, then libev will not attempt to use the
    ``inotify`` API for the :py:class:`Stat` watchers. Apart from debugging and
    testing, this flag can be useful to conserve ``inotify`` file descriptors,
    as otherwise each loop using :py:class:`Stat` watchers consumes one
    ``inotify`` handle.

.. py:data:: EVFLAG_SIGNALFD

    When this flag is specified, then libev will attempt to use the ``signalfd``
    API for the :py:class:`Signal` (and :py:class:`Child`) watchers. This API
    delivers signals synchronously, which makes it both faster and might make it
    possible to get the queued signal data. It can also simplify signal handling
    with threads, as long as you properly block signals in your threads that are
    not interested in handling them.
    ``signalfd`` will not be used by default as this changes your signal mask.

.. py:data:: EVFLAG_NOSIGMASK

    When this flag is specified, then libev will avoid to modify the signal mask.
    Specifically, this means you have to make sure signals are unblocked when
    you want to receive them.
    This behaviour is useful when you want to do your own signal handling, or
    want to handle signals only in specific threads and want to avoid libev
    unblocking the signals.
    It's also required by POSIX in a threaded program, as libev calls
    :c:func:`sigprocmask`, whose behaviour is officially unspecified.
    This flag's behaviour will become the default in future versions of libev.



.. _Loop_backends:

backends
--------

.. py:data:: EVBACKEND_SELECT

    *Availability:* POSIX, Windows

    The standard ``select`` backend. Not completely standard, as libev tries to
    roll its own :c:type:`fd_set` with no limits on the number of fds, but if
    that fails, expect a fairly low limit on the number of fds when using this
    backend. It doesn't scale too well (O(highest_fd)), but is usually the
    fastest backend for a low number of fds.

    To get good performance out of this backend you need a high amount of
    parallelism (most of the file descriptors should be busy). If you are
    writing a server, you should :c:func:`accept` in a loop to accept as many
    connections as possible during one iteration. You might also want to have a
    look at :py:attr:`Loop.io_interval` to increase the amount of readiness
    notifications you get per iteration.

    This backend maps :py:const:`EV_READ` to the :c:data:`readfds` set and
    :py:const:`EV_WRITE` to the :c:data:`writefds` set (and to work around
    Microsoft Windows bugs, also onto the :c:data:`exceptfds` set on that
    platform).

.. py:data:: EVBACKEND_POLL

    *Availability:* POSIX

    The ``poll`` backend. It's more complicated than ``select``, but handles
    sparse fds better and has no artificial limit on the number of fds you can
    use (except it will slow down considerably with a lot of inactive fds). It
    scales similarly to ``select``, i.e. O(total_fds). See
    :py:const:`EVBACKEND_SELECT`, above, for performance tips.

    This backend maps :py:const:`EV_READ` to
    :c:data:`POLLIN` | :c:data:`POLLERR` | :c:data:`POLLHUP`, and
    :py:const:`EV_WRITE` to
    :c:data:`POLLOUT` | :c:data:`POLLERR` | :c:data:`POLLHUP`.

.. py:data:: EVBACKEND_EPOLL

    *Availability:* Linux

    Use the linux-specific ``epoll`` interface. For few fds, this backend is a
    little bit slower than ``poll`` and ``select``, but it scales phenomenally
    better. While ``poll`` and ``select`` usually scale like O(*n*) where *n* is
    the total number of fds (or the highest fd), ``epoll`` scales either O(1) or
    O(active_fds).

    While stopping, setting and starting an I/O watcher in the same iteration
    will result in some caching, there is still a system call per such incident,
    so its best to avoid that. Also, :c:func:`dup`'ed file descriptors might not
    work very well if you register events for both file descriptors.

    Best performance from this backend is achieved by not unregistering all
    watchers for a file descriptor until it has been closed, if possible, i.e.
    keep at least one watcher active per fd at all times. Stopping and starting
    a watcher (without re-setting it) also usually doesn't cause extra overhead.
    A fork can both result in spurious notifications as well as in libev having
    to destroy and recreate the ``epoll`` object, which can take considerable
    time and thus should be avoided. All this means that, in practice,
    ``select`` can be as fast or faster than ``epoll`` for maybe up to a hundred
    file descriptors, depending on the usage.

    While nominally embeddable in other event loops, this feature is disabled in
    kernels < 2.6.32.

    This backend maps :py:const:`EV_READ` and :py:const:`EV_WRITE` the same way
    :py:const:`EVBACKEND_POLL` does.

.. py:data:: EVBACKEND_KQUEUE

    *Availability:* most BSD clones

    Due to a number of bugs and inconsistencies between BSDs implementations,
    ``kqueue`` is not being 'auto-detected' unless you explicitly specify it in
    the *flags* or libev was compiled on a known-to-be-good (-enough) system
    like NetBSD. It scales the same way the ``epoll`` backend does.

    While stopping, setting and starting an I/O watcher does never cause an
    extra system call as with :py:const:`EVBACKEND_EPOLL`, it still adds up to
    two event changes per incident. Support for :c:func:`fork` is bad (but sane)
    and it drops fds silently in similarly hard-to-detect cases.

    This backend usually performs well under most conditions.

    You still can embed ``kqueue`` into a normal ``poll`` or ``select`` backend
    and use it only for sockets (after having made sure that sockets work with
    ``kqueue`` on the target platform). See :py:class:`Embed` watchers for more
    info.

    This backend maps :py:const:`EV_READ` into an :c:data:`EVFILT_READ` kevent
    with :c:data:`NOTE_EOF`, and :py:const:`EV_WRITE` into an
    :c:data:`EVFILT_WRITE` kevent with :c:data:`NOTE_EOF`.

.. py:data:: EVBACKEND_DEVPOLL

    *Availability:* Solaris 8

    This is not implemented yet (and might never be). According to reports,
    ``/dev/poll`` only supports sockets and is not embeddable, which would limit
    the usefulness of this backend immensely.

.. py:data:: EVBACKEND_PORT

    *Availability:* Solaris 10

    This uses the Solaris 10 ``event port`` mechanism. It's slow, but it scales
    very well (O(active_fds)).

    It requires one system call per active file descriptor per loop iteration.
    For a small to medium number of file descriptors, a 'slow'
    :py:const:`EVBACKEND_SELECT` or :py:const:`EVBACKEND_POLL` backend might
    perform better.

    On the positive side, this backend actually performed fully to specification
    in all tests and is fully embeddable.

    This backend maps :py:const:`EV_READ` and :py:const:`EV_WRITE` the same way
    :py:const:`EVBACKEND_POLL` does.

.. py:data:: EVBACKEND_ALL

    Try all backends (even potentially broken ones that wouldn't be tried with
    :py:const:`EVFLAG_AUTO`). Since this is a mask, you can do stuff such as::

        pyev.EVBACKEND_ALL & ~pyev.EVBACKEND_KQUEUE

    It is definitely not recommended to use this flag, use whatever
    :py:func:`recommended_backends` returns, or simply do not specify a backend
    at all.

.. py:data:: EVBACKEND_MASK

    Not a backend at all, but a mask to select all backend bits from a flags
    value, in case you want to mask out any backends from a flags value
    (e.g. when modifying the :envvar:`LIBEV_FLAGS` environment variable).


.. _Loop_start_flags:

:py:meth:`Loop.start` *flags*
=============================

If *flags* is omitted or specified as ``0``, it will keep handling events until
either no event watchers are active anymore or :py:meth:`Loop.stop` was called.

.. py:data:: EVRUN_NOWAIT

    A *flags* value of :py:const:`EVRUN_NOWAIT` will look for new events,
    will handle those events and any already outstanding ones, but will not
    wait and block your process in case there are no events and will return
    after one iteration of the loop.
    This is sometimes useful to poll and handle new events while doing lengthy
    calculations, to keep the program responsive.

.. py:data:: EVRUN_ONCE

    A *flags* value of :py:const:`EVRUN_ONCE` will look for new events
    (waiting if necessary) and will handle those and any already outstanding
    ones. It will block your process until at least one new event arrives
    (which could be an event internal to libev itself, so there is no
    guarantee that a user-registered callback will be called), and will
    return after one iteration of the loop.
    This is useful if you are waiting for some external event in conjunction
    with something not expressible using other libev watchers. However, a pair
    of :py:class:`Prepare`\ /\ :py:class:`Check` watchers is usually a better
    approach for this kind of thing.

.. note::
    An explicit :py:meth:`Loop.stop` is usually better than relying on all
    watchers being stopped when deciding if a program has finished (especially
    in interactive programs).


.. _Loop_stop_how:

:py:meth:`Loop.stop` *how*
==========================

.. py:data:: EVBREAK_ONE

    If *how* is omitted or specified as :py:const:`EVBREAK_ONE` it will make the
    innermost :py:meth:`Loop.start` call return.

.. py:data:: EVBREAK_ALL

    A *how* value of :py:const:`EVBREAK_ALL` will make all nested
    :py:meth:`Loop.start` calls return.


.. _Loop_watcher_methods:

:py:class:`Loop` watcher methods
================================

The following methods are just a convenient way to instantiate watchers attached
to the loop (although they do not take keyword arguments).

.. py:method:: Loop.io(fd, events, callback[, data, priority])

    Returns an :py:class:`Io` object.

.. py:method:: Loop.timer(after, repeat, callback[, data, priority])

    Returns a :py:class:`Timer` object.

.. py:method:: Loop.periodic(offset, interval, callback[, data, priority])

    Returns a :py:class:`Periodic` object.

.. py:method:: Loop.scheduler(scheduler, callback[, data, priority])

    Returns a :py:class:`Scheduler` object.

.. py:method:: Loop.signal(signum, callback[, data, priority])

    Returns a :py:class:`Signal` object.

.. py:method:: Loop.child(pid, trace, callback[, data, priority])

    Returns a :py:class:`Child` object.

.. py:method:: Loop.stat(path, interval, callback[, data, priority])

    Returns a :py:class:`Stat` object.

.. py:method:: Loop.idle(callback[, data, priority])

    Returns an :py:class:`Idle` object.

.. py:method:: Loop.prepare(callback[, data, priority])

    Returns a :py:class:`Prepare` object.

.. py:method:: Loop.check(callback[, data, priority])

    Returns a :py:class:`Check` object.

.. py:method:: Loop.embed(other[, callback, data, priority])

    Returns an :py:class:`Embed` object.

.. py:method:: Loop.fork(callback[, data, priority])

    Returns a :py:class:`Fork` object.

.. py:method:: Loop.async(callback[, data, priority])

    Returns an :py:class:`Async` object.
