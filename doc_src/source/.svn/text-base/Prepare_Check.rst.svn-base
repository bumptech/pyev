.. _Prepare_Check:


.. currentmodule:: pyev


========================================================================
:py:class:`Prepare`\ /\ :py:class:`Check` --- Prepare and Check watchers
========================================================================


.. py:class:: Prepare(loop, callback[, data=None, priority=0])

.. py:class:: Check(loop, callback[, data=None, priority=0])

    :type loop: :py:class:`Loop`
    :param loop: loop object responsible for this watcher (accessible through
        :py:attr:`Watcher.loop`).

    :param callable callback: See :py:attr:`Watcher.callback`.

    :param object data: any Python object you might want to attach to the
        watcher (stored in :py:attr:`Watcher.data`).

    :param int priority: See :py:attr:`Watcher.priority`.

    :py:class:`Prepare` and :py:class:`Check` watchers are usually (but not
    always) used in pairs: :py:class:`Prepare` watchers get invoked before the
    process blocks and :py:class:`Check` watchers afterwards.

    You must not call :py:meth:`Loop.start` or similar methods that enter the
    current event loop from either :py:class:`Prepare` or :py:class:`Check`
    watchers. Other loops than the current one are fine, however. The rationale
    behind this is that you do not need to check for recursion in those
    watchers, i.e. the sequence will always be: :py:class:`Prepare` -> blocking
    -> :py:class:`Check`, so if you have one watcher of each kind they will
    always be called in pairs bracketing the blocking call.

    Their main purpose is to integrate other event mechanisms into libev and
    their use is somewhat advanced. They could be used, for example, to track
    variable changes, implement your own watchers, integrate net-snmp or a
    coroutine library and lots more. They are also occasionally useful if you
    cache some data and want to flush it before blocking.

    It is recommended to give :py:class:`Check` watchers highest
    (:py:const:`EV_MAXPRI`) priority, to ensure that they are being run before
    any other watchers after the poll (this doesn't matter for
    :py:class:`Prepare` watchers).

    Also, :py:class:`Check` watchers (and :py:class:`Prepare` watchers, too)
    should not activate/feed events into libev. While libev fully supports this,
    they might get executed before other :py:class:`Check` watchers did their
    job.

    .. seealso::
        `ev_prepare and ev_check - customise your event loop!
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_prepare_code_and_code_ev_che>`_
