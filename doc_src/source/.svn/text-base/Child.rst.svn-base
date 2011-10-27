.. _Child:


.. currentmodule:: pyev


===================================
:py:class:`Child` --- Child watcher
===================================


.. py:class:: Child(pid, trace, loop, callback[, data=None, priority=0])

    :param int pid: wait for status changes of process *pid* (or any process
        if *pid* is specified as ``0``).

    :param bool trace: if :py:const:`False` only activate the watcher when
        the process terminates, if :py:const:`True` additionally activate
        the watcher when the process is stopped or continued.

    :type loop: :py:class:`Loop`
    :param loop:  **must be the default loop**. loop object responsible for this
        watcher (accessible through :py:attr:`Watcher.loop`).

    :param callable callback: See :py:attr:`Watcher.callback`.

    :param object data: any Python object you might want to attach to the
        watcher (stored in :py:attr:`Watcher.data`).

    :param int priority: See :py:attr:`Watcher.priority`.

    :py:class:`Child` watchers trigger when your process receives a
    :c:data:`SIGCHLD` in response to some child status changes (most typically
    when a child of yours dies or exits). It is permissible to install a
    :py:class:`Child` watcher after the child has been forked (which implies it
    might have already exited), as long as the event loop isn't entered (or is
    continued from a watcher), i.e. forking and then immediately registering a
    watcher for the child is fine, but forking and registering a watcher a few
    event loop iterations later or in the next callback invocation is not.

    You can only register :py:class:`Child` watchers in the *default loop*.

    Due to some design glitches inside libev, child watchers will always be
    handled at maximum priority (their priority is set to :py:const:`EV_MAXPRI`
    by libev).

    .. seealso::
        `ev_child - watch out for process status changes
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_child_code_watch_out_for_pro>`_

            * `Process Interaction
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Process_Interaction>`_
            * `Overriding the Built-In Processing
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Overriding_the_Built_In_Processing>`_
            * `Stopping the Child Watcher
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Stopping_the_Child_Watcher>`_


    .. py:method:: set(pid, trace)

        :param int pid: wait for status changes of process *pid* (or any process
            if *pid* is specified as ``0``).

        :param bool trace: if :py:const:`False` only activate the watcher when
            the process terminates, if :py:const:`True` additionally activate
            the watcher when the process is stopped or continued.

        Configures the watcher.


    .. py:attribute:: pid

        *Read only*

        The process id this watcher watches out for, or ``0``, meaning any
        process id.


    .. py:attribute:: rpid

        The process id that detected a status change.


    .. py:attribute:: rstatus

        The process exit status caused by :py:attr:`rpid`.
