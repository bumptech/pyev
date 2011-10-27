.. _Embed:


.. currentmodule:: pyev


===================================
:py:class:`Embed` --- Embed watcher
===================================


.. py:class:: Embed(other, loop[, callback=None, data=None, priority=0])

    :type other: :py:class:`Loop`
    :param other: the loop to embed, this loop must be embeddable (i.e. its
        backend must be in the set of :py:func:`embeddable_backends`).

    :type loop: :py:class:`Loop`
    :param loop: loop object responsible for this watcher (accessible through
        :py:attr:`Watcher.loop`).

    :type callback: callable or None
    :param callback: See :py:attr:`callback`.

    :param object data: any Python object you might want to attach to the
        watcher (stored in :py:attr:`Watcher.data`).

    :param int priority: See :py:attr:`Watcher.priority`.

    This is a rather advanced watcher type that lets you embed one event loop
    into another (currently only :py:class:`Io` events are supported in the
    embedded loop, other types of watchers might be handled in a delayed or
    incorrect fashion and must not be used).

    There are primarily two reasons you would want that: work around bugs and
    prioritise I/O.

    As an example for a bug workaround, the ``kqueue`` backend might only
    support sockets on some platform, so it is unusable as generic backend, but
    you still want to make use of it because you have many sockets and it scales
    so nicely. In this case, you would create a kqueue-based loop and embed it
    into your default loop (which might use e.g. ``poll``). Overall operation
    will be a bit slower because first libev has to call poll and then kevent,
    but at least you can use both mechanisms for what they are best: ``kqueue``
    for scalable sockets and ``poll`` if you want it to work :)

    As for prioritising I/O: under rare circumstances you have the case where
    some fds have to be watched and handled very quickly (with low latency), and
    even priorities and :py:class:`Idle` watchers might have too much overhead.
    In this case you would put all the high priority stuff in one loop and all
    the rest in a second one, and embed the second one in the first.

    Fork detection will be handled transparently while the :py:class:`Embed`
    watcher is active, i.e., the embedded loop will automatically be forked when
    the embedding loop forks. When the watcher is not running, however, it is
    still the task of the libev user to call :py:meth:`Loop.fork` as applicable.

    Unfortunately, not all backends are embeddable: only the ones returned by
    :py:func:`embeddable_backends` are, which, unfortunately, does not include
    any portable one.

    .. seealso::
        `ev_embed - when one backend isn't enough...
        <http://pod.tst.eu/http://cvs.schmorp.de/libev/ev.pod#code_ev_embed_code_when_one_backend_>`_


    .. py:method:: set(other)

        :type other: :py:class:`Loop`
        :param other: the loop to embed, this loop must be embeddable (i.e. its
            backend must be in the set of :py:func:`embeddable_backends`).

        Configures the watcher.


    .. py:method:: sweep

        Make a single, non-blocking sweep over the embedded loop. This works
        similarly to::

            other.start(pyev.EVRUN_NOWAIT)

        but in the most appropriate way for embedded loops.


    .. py:attribute:: other

        *Read only*

        The embedded event loop.


    .. py:attribute:: callback

        As long as the watcher is active, the callback will be invoked every
        time there might be events pending in the embedded loop. The callback
        must then call :py:meth:`sweep` to make a single sweep and invoke their
        callbacks (the callback doesn't need to invoke the :py:meth:`sweep`
        method directly, it could also start an :py:class:`Idle` watcher to give
        the embedded loop strictly lower priority for example).

        You can also set the callback to :py:const:`None`, in which case the
        :py:class:`Embed` watcher will automatically execute the embedded loop
        sweep whenever necessary.

        See also :py:attr:`Watcher.callback`.
