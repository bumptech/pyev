Python libev interface.

libev is an event loop: you register interest in certain events (such as a file
descriptor being readable or a timeout occurring), and it will manage these
event sources and provide your program with events.
To do this, it must take more or less complete control over your process (or
thread) by executing the event loop handler, and will then communicate events
via a callback mechanism.
You register interest in certain events by registering so-called event watchers,
which you initialise with the details of the event, and then hand over to libev
by starting the watcher.

libev supports ``select``, ``poll``, the Linux-specific ``epoll``, the
BSD-specific ``kqueue`` and the Solaris-specific ``event port`` mechanisms for
file descriptor events (:py:class:`Io`), the Linux ``inotify`` interface (for
:py:class:`Stat`), Linux ``eventfd``/``signalfd`` (for faster and cleaner
inter-thread wakeup (:py:class:`Async`)/signal handling (:py:class:`Signal`)),
relative timers (:py:class:`Timer`), absolute timers (:py:class:`Periodic`),
timers with customised rescheduling (:py:class:`Scheduler`), synchronous signals
(:class:`Signal`), process status change events (:py:class:`Child`), and event
watchers dealing with the event loop mechanism itself (:py:class:`Idle`,
:py:class:`Embed`, :py:class:`Prepare` and :py:class:`Check` watchers) as well
as file watchers (:py:class:`Stat`) and even limited support for fork events
(:py:class:`Fork`).

It also is quite `fast <http://libev.schmorp.de/bench.html>`_.

libev is written and maintained by Marc Lehmann.

.. seealso::
    `libev's homepage <http://software.schmorp.de/pkg/libev>`_.


Useful links:

- `Latest release <http://pypi.python.org/pypi/pyev/>`_
- `Documentation <http://packages.python.org/pyev/>`_
- `Bug reports and feature requests
  <http://code.google.com/p/pyev/issues/list>`_


`pyev's source code <http://pyev.googlecode.com/>`_ is currently hosted by
`Google code <http://code.google.com/>`_ and kept in a
`Subversion <http://subversion.apache.org/>`_ repository.

- `Subversion instructions <http://code.google.com/p/pyev/source/checkout>`_
- `Subversion browser <http://code.google.com/p/pyev/source/browse/>`_
