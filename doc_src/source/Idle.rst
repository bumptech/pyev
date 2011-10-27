.. _Idle:


.. currentmodule:: pyev


=================================
:py:class:`Idle` --- Idle watcher
=================================


.. py:class:: Idle(loop, callback[, data=None, priority=0])

    :type loop: :py:class:`Loop`
    :param loop: loop object responsible for this watcher (accessible through
        :py:attr:`Watcher.loop`).

    :param callable callback: See :py:attr:`Watcher.callback`.

    :param object data: any Python object you might want to attach to the
        watcher (stored in :py:attr:`Watcher.data`).

    :param int priority: See :py:attr:`Watcher.priority`.

    :py:class:`Idle` watchers trigger events when no other events of the same or
    higher priority are pending (:py:class:`Prepare`, :py:class:`Check` and
    other :py:class:`Idle` watchers do not count as receiving 'events').

    That is, as long as your process is busy handling sockets or timeouts (or
    even signals) of the same or higher priority it will not be triggered. But
    when your process is idle (or only lower-priority watchers are pending), the
    :py:class:`Idle` watchers are being called once per event loop iteration -
    until stopped, that is, or your process receives more events and becomes
    busy again with higher priority stuff.

    The most noteworthy effect is that as long as any idle watchers are active,
    the process will not block when waiting for new events.

    Apart from keeping your process non-blocking (which is a useful effect on
    its own sometimes), :py:class:`Idle` watchers are a good place to do
    'pseudo-background processing', or delay processing stuff to after the event
    loop has handled all outstanding events.

    .. seealso::
        `ev_idle - when you've got nothing better to do...
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_idle_code_when_you_ve_got_no>`_
