
:Notes-By:
    Bryce Keen

Memory
======

.. math::

    Miss Rate = (Number of misses)/(Number of total memory accesses) = 1 - Hit Rate

Cache
-----

| **Temporal Locality** - The processor is likely to access a piece of data again soon if has accessed that data recently 
| **Spatial Locality** - If the processor accesses a piece of data then it is likely to access data nearby

    Therefore if one word is fetched from memory a few adjacent words are also fetched. This is called a *cache block* or *cache line* with the number of words in the blocks called the *block size*. 


	| :math:`C` = *Cache Capacity*
	| :math:`B` = *Cache Blocks/Lines*
	| :math:`b` = *Block Size*

.. math::

    C = B*b 	

| **Sets** - A cache is is organized into sets which hold one or more cache blocks.
    

    - **Direct Mapped Cache** - Each *set* holds only one *cache block*.
    - **N-way Set Associative Cache** - Each *set* holds *N* number of *cache blocks*.
    - **Fully Associative Cache** -
    - **B-way Cache** - 

    :math:`S` = *Sets*    

Direct Mapped Cache
^^^^^^^^^^^^^^^^^^^

A *direct mapped* cache has one 

