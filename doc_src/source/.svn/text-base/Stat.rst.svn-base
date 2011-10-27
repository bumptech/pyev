.. _Stat:


.. currentmodule:: pyev


=================================
:py:class:`Stat` --- Stat watcher
=================================


.. py:class:: Stat(path, interval, loop, callback[, data=None, priority=0])

    :param path: wait for status changes of the given *path*.

    :param float interval: hint on how quickly a change is expected to be
        detected and should normally be specified as ``0.0`` to let libev
        choose a suitable value.

    :type loop: :py:class:`Loop`
    :param loop: loop object responsible for this watcher (accessible through
        :py:attr:`Watcher.loop`).

    :param callable callback: See :py:attr:`Watcher.callback`.

    :param object data: any Python object you might want to attach to the
        watcher (stored in :py:attr:`Watcher.data`).

    :param int priority: See :py:attr:`Watcher.priority`.

    This watches a file system path for attribute changes. That is, it calls
    :c:func:`stat` on that path in regular intervals (or when the OS says it
    changed) and sees if it changed compared to the last time, invoking the
    callback if it did.

    The path does not need to exist: changing from 'path exists' to 'path does
    not exist' is a status change like any other. The condition 'path does not
    exist' (or more correctly 'path cannot be :c:func:`stat`\ ed') is signified
    by the :py:attr:`Statdata.nlink` field being ``0`` (which is otherwise
    always forced to be at least ``1``) and all the other fields of the
    :py:class:`Statdata` object having unspecified contents.

    The path must not end in a slash or contain special components such as ``.``
    or ``..``. The path should be absolute: if it is relative and your working
    directory changes, then the behaviour is undefined.

    Since there is no portable change notification interface available, the
    portable implementation simply calls :c:func:`stat` regularly on the path to
    see if it changed somehow. You can specify a recommended polling interval
    for this case. If you specify a polling interval of ``0.0`` (highly
    recommended!) then a suitable, unspecified default value will be used (which
    you can expect to be around five seconds, although this might change
    dynamically). libev will also impose a minimum interval which is currently
    around ``0.1``, but that's usually overkill.

    This watcher type is not meant for massive numbers of :py:class:`Stat`
    watchers, as even with OS-supported change notifications, this can be
    resource-intensive.

    .. seealso::
        `ev_stat - did the file attributes just change?
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_stat_code_did_the_file_attri>`_

            * `Inotify and Kqueue
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#Inotify_and_Kqueue>`_
            * `stat () is a synchronous operation
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_stat_code_is_a_synchronous_oper>`_
            * `The special problem of stat time resolution
              <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#The_special_problem_of_stat_time_res>`_


    .. py:method:: set(path, interval)

        :param path: wait for status changes of the given *path*.

        :param float interval: hint on how quickly a change is expected to be
            detected and should normally be specified as ``0.0`` to let libev
            choose a suitable value.

        Configures the watcher.


    .. py:method:: stat

        Updates :py:attr:`Stat.current` immediately with a new
        :py:class:`Statdata` object. If you change the watched path in your
        callback, you could call this function to avoid detecting this change
        (while introducing a race condition if you are not the only one changing
        the path). Can also be useful simply to find out the new values.


    .. py:attribute:: path

        *Read only*

        The file system path that is being watched.


    .. py:attribute:: interval

        *Read only*

        The specified interval.


    .. py:attribute:: current

        *Read only*

        Current :py:class:`Statdata`. If the :py:attr:`~Statdata.nlink`
        attribute is ``0``, then there was some error while stating the file.


    .. py:attribute:: previous

        *Read only*

        Previous :py:class:`Statdata`. The callback gets invoked whenever
        :py:attr:`Stat.previous` != :py:attr:`Stat.current`, or, more precisely,
        one or more of these attributes differ: :py:attr:`~Statdata.dev`,
        :py:attr:`~Statdata.ino`, :py:attr:`~Statdata.mode`,
        :py:attr:`~Statdata.nlink`, :py:attr:`~Statdata.uid`,
        :py:attr:`~Statdata.gid`, :py:attr:`~Statdata.rdev`,
        :py:attr:`~Statdata.size`, :py:attr:`~Statdata.atime`,
        :py:attr:`~Statdata.mtime`, :py:attr:`~Statdata.ctime`.


:py:class:`Statdata`
====================


.. py:class:: Statdata


    .. py:attribute:: dev

        *Read only*

        device.


    .. py:attribute:: rdev

        *Read only*

        device type.


    .. py:attribute:: ino

        *Read only*

        inode.


    .. py:attribute:: size

        *Read only*

        total size, in bytes.


    .. py:attribute:: nlink

        *Read only*

        number of hard links.


    .. py:attribute:: mode

        *Read only*

        protection bits.


    .. py:attribute:: uid

        *Read only*

        user ID of owner.


    .. py:attribute:: gid

        *Read only*

        group ID of owner.


    .. py:attribute:: atime

        *Read only*

        time of last access.


    .. py:attribute:: mtime

        *Read only*

        time of last modification.


    .. py:attribute:: ctime

        *Read only*

        time of last status change.
