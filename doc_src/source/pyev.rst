.. _pyev:


******************************************
:py:mod:`pyev` --- Python libev interface.
******************************************

.. py:module:: pyev
    :platform: POSIX, Windows
    :synopsis: Python libev interface.

.. seealso::
    `libev's documentation
    <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod>`_.


.. py:function:: default_loop([flags=EVFLAG_AUTO, callback=None, data=None, debug=False, io_interval=0.0, timeout_interval=0.0]) -> the 'default loop'

    This will instanciate the *default loop* if it hasn't been created yet
    and return it. If the *default loop* was already initialized this simply
    returns it (and ignores the arguments).

    The *default loop* is the only loop that can handle :py:class:`Child`
    watchers, and to do this, it always registers a handler for
    :c:data:`SIGCHLD`. If this is a problem for your application you can either
    instanciate a :py:class:`Loop` which doesn't do that, or you can simply
    overwrite the :c:data:`SIGCHLD` signal handler.

    See :py:class:`Loop` for details about the arguments.

    .. note::
         If you don't know what loop to use, use the one returned from this
         function.


.. py:function:: supported_backends() -> int

    Returns the set of all backends (i.e. their corresponding EVBACKEND_* value)
    compiled into this binary of libev (independent of their availability on the
    system you are running on).

    See :ref:`Loop_backends` for a description of the set values.


.. py:function:: recommended_backends() -> int

    Returns the set of all backends compiled into this binary of libev and also
    recommended for this platform, meaning it will work for most file descriptor
    types. This set is often smaller than the one returned by
    :py:func:`supported_backends`, as for example ``kqueue`` is broken on most
    BSDs and will not be auto-detected unless you explicitly request it.
    This is the set of backends that libev will probe for you if you specify no
    backends explicitly.

    See :ref:`Loop_backends` for a description of the set values.


.. py:function:: embeddable_backends() -> int

    Returns the set of backends that are embeddable in other event loops.
    This value is platform-specific but can include backends not available on
    the current system. To find which embeddable backends might be supported on
    the current system, you would need to look at::

        pyev.embeddable_backends() & pyev.supported_backends()

    likewise for recommended ones::

        pyev.embeddable_backends() & pyev.recommended_backends()

    See :ref:`Loop_backends` for a description of the set values.


.. py:function:: time() -> float

    Returns the current time as libev would use it.

    .. note::
         The :py:meth:`Loop.now` method is usually faster and also often returns
         the timestamp you actually want to know.


.. py:function:: sleep(interval)

    :param float interval: interval in seconds.

    Sleep for the given *interval*. The current thread will be blocked until
    either it is interrupted or the given time interval has passed.


.. py:function:: feed_signal(signum)

    :param int signum: signal number to feed libev.

    This function can be used to 'simulate' a signal receive. It is completely
    safe to call this function at any time, from any context, including signal
    handlers or random threads. Its main use is to customise signal handling in
    your process, especially in the presence of threads.

    For example, using the :py:mod:`signal` module, you could ignore signals by
    default in all threads (and specify :py:const:`EVFLAG_NOSIGMASK` when
    creating any loops), and in one thread, wait for signals, then 'deliver'
    them to libev by calling :py:func:`feed_signal`.


.. py:function:: abi_version() -> tuple of ints

    Returns a tuple of major, minor version numbers. These numbers represent the
    libev ABI version that this module is running.

    .. note::
        This is not the same as libev version (although it might coincide).


.. py:function:: version() -> tuple of strings

    Returns a tuple of version strings. The former is pyev version, while the
    latter is the underlying libev version.


.. py:exception:: Error

    Raised when an error specific to pyev happens.


Objects
*******

.. toctree::
    :maxdepth: 2
    :titlesonly:

    Loop
    Watcher
