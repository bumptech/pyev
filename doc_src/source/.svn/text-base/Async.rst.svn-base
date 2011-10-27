.. _Async:


.. currentmodule:: pyev


===================================
:py:class:`Async` --- Async watcher
===================================


.. py:class:: Async(loop, callback[, data=None, priority=0])

    :type loop: :py:class:`Loop`
    :param loop: loop object responsible for this watcher (accessible through
        :py:attr:`Watcher.loop`).

    :param callable callback: See :py:attr:`Watcher.callback`.

    :param object data: any Python object you might want to attach to the
        watcher (stored in :py:attr:`Watcher.data`).

    :param int priority: See :py:attr:`Watcher.priority`.

    In general, you cannot use a :py:class:`Loop` from multiple threads or other
    asynchronous sources such as signal handlers (as opposed to multiple event
    loops - those are of course safe to use in different threads).

    Sometimes, however, you need to wake up an event loop you do not control,
    for example because it belongs to another thread. This is what
    :py:class:`Async` watchers do: as long as the :py:class:`Async` watcher is
    active, you can signal it by calling :py:meth:`send`, which is thread- and
    signal safe.

    This functionality is very similar to :py:class:`Signal` watchers, as
    signals, too, are asynchronous in nature, and signals, too, will be
    compressed (i.e. the number of callback invocations may be less than the
    number of :py:meth:`send` calls). In fact, you could use signal watchers as
    a kind of 'global async watchers' by using a watcher on an otherwise unused
    signal, and signal this watcher from another thread, even without knowing
    which loop owns the signal.

    .. seealso::
        `ev_async - how to wake up an event loop
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_async_code_how_to_wake_up_an>`_

            * `Queueing
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Queueing>`_


    .. py:method:: send

        Sends/signals/activates the :py:class:`Async` watcher, that is, feeds an
        :py:const:`EV_ASYNC` event on the watcher into the event loop, and
        returns immediately.

        Note that, as with other watchers in libev, multiple events might get
        compressed into a single callback invocation (another way to look at
        this is that :py:class:`Async` watchers are level-triggered, set on
        :py:meth:`send`, reset when the event loop detects that).

        This call incurs the overhead of a system call only once per event loop
        iteration, so while the overhead might be noticeable, it doesn't apply
        to repeated calls to :py:meth:`send` for the same event loop.


    .. py:attribute:: sent

        *Read only*

        :py:const:`True` if :py:meth:`send` has been called on the watcher but
        the event has not yet been processed (or even noted) by the event loop,
        :py:const:`False` otherwise.

        .. note::
            This does not check whether the watcher itself is pending, only
            whether it has been requested to make this watcher pending.
