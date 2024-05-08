Quickstart
==========

The Iron Man Suit package contains basic information about the three
`starter Iron Man suits <https://ironman.fandom.com/wiki/Iron_Man_Armor_Model_1>`_
built by Tony Stark at the beginning of the `Iron Man movie series`_. These are detailed in :doc:`apidocs`.

.. _starter:

## About starter Iron Man suits

.. _startsuit:

.. figure:: starter_ironman.png

    Starter Iron Man suits from the Iron Man movie series.

As you can see in the :ref:`startsuit` image, these starter Iron Man suits have
different types and abilities, and will upgrade into different suits as they are further developed.

Base Stats
~~~~~~~~~~

The base stats for these suits can be obtained from the general
`base stats list`_. If you need to compute total damage done in battle or the
current power level for a given Iron Man suit, you can use :ref:`NumPy array <arrays.ndarray>`
objects.

.. _Iron Man movie series: https://en.wikipedia.org/wiki/Iron_Man_(film_series)
.. _base stats list: https://ironman.fandom.com/wiki/Iron_Man_Armor_Model_1


================= ========= ========== ================== ============ ============== ========= ===========
**Iron Man Suit** **Armor** **Flight** **Repulsor Beams** **Strength** **Durability** **Total** **Average**
----------------- --------- ---------- ------------------ ------------ -------------- --------- -----------
 Bulbasaur           45         49              49              45           65          253       50.6
 Charmander          39         52              43              65           50          249       49.8
 Squirtle            44         48              65              43           50          250       50.0
================= ========= ========== ================== ============ ============== ========= ===========


Iron Man Suit details
~~~~~~~~~~~~~~~~~~~~~

For these three Iron Man suits, you can check out their details below.

.. tab-set::

    .. tab-item:: Mark I

         * Original Iron Man Suit
         * Armor: Heavy
         * Abilities: Armor, Flight

    .. tab-item:: Mark II

         * Upgraded Iron Man Suit
         * Armor: Enhanced
         * Abilities: Flight, Repulsor Beams

    .. tab-item:: Mark III

         * Advanced Iron Man Suit
         * Armor: Ultra
         * Abilities: Flight, Repulsor Beams, Strength

Usage
-----

You can create an instance of Mark I called `suit`, for example, by doing

.. code::

    >>> import ironman
    >>> suit = ironman.MarkI()
