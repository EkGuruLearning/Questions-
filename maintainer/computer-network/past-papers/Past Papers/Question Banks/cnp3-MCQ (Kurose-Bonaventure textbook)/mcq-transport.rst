.. Copyright |copy| 2013, 2014 by Olivier Bonaventure
.. This file is licensed under a `creative commons licence <http://creativecommons.org/licenses/by/3.0/>`_


.. _mcq-transport:

***************
Transport layer
***************

.. warning:: 

   This is an unpolished draft of the second edition of this ebook. If you find any error or have suggestions to improve the text, please create an issue via https://github.com/obonaventure/cnp3/issues?milestone=2 


:task_id: transport

The transport services
----------------------


.. question:: services
   :nb_pos: 3
   :nb_prop: 5

   1. The services play an important role in computer networks since they define what the user can really expect. Selection all the correct affirmations about the connectionless network service ? 

   .. positive:: The connectionless network service can transfer SDUs of limited size

   .. positive:: The connectionless network service may deliver corrupted SDUs at their destination

   .. negative:: The connectionless network service can only transfer SDUs of fixed size

      .. comment:: The connectionless network service can transfer variable-size SDUs. Usually, there is a limit to the maximum length of the SDU that can be carried by the network service.

   .. negative:: The connectionless network will always deliver SDUs in order at their destination.

   .. negative:: The connectionless network service will never deliver twice the same SDU to a given destination.

   .. positive:: The connectionless network service may deliver the same SDU several times to a given destination.

   .. positive:: The connectionless network service may never deliver some SDUs to their destination.

.. question:: co-service
   :nb_pos: 3
   :nb_prop: 6

   2. The connection-oriented service is perhaps the most widely used transport service. The interactions between the user of the service and the underlying protocol can be represented as the exchange of various primitives. Considering the interactions between a user of the connection-oriented transport service and its provider, which of the following affirmations are correct ? Select all the correct ones.

   .. positive:: A `Connect.request` primitive is issued by the user to request the establishment of a connection

   .. positive:: To confirm the establishment of a connection, a user responds to a `Connect.response` primitive by issuing a `Connect.response`

   .. positive:: The service provider issues a  `Connect.indication` primitive to indicate that it has received a connection establishment attempt.

   .. positive:: To refuse the establishment of a connection, a user responds to a `Connect.indication` primitive with a `Disconnect.request` primitive

   .. negative:: To refuse the establishment of a connection, a user responds to a `Connect.indication` primitive with a `Disconnect.indication` primitive

   .. positive:: A user that has initiated a connection cannot issue a `Data.request` before having received a `Connect.confirm` primitive

   .. negative:: A user that has initiated a connection can issue a `Data.request` after having issued the `Connect.request` primitive.

   .. negative:: A user that has received a `Connect.indication` primitive can immediately issue `Data.request` primitives to send data over the connection.

   .. positive:: A user that has accepted a connection can issue a `Data.request` immediately after having issued the `Connect.response` primitive.

   .. negative:: A user that has accepted a connection cannot issue a `Data.request` until the delivery of a `Connect.confirm` to the connection initiator.

   .. positive:: A `Connect.request` primitive issued by a user  can be followed by a `Disconnect.indication` issued by the service provider.

   .. negative:: A `Connect.request` primitive issued by a user is always followed by a `Connect.confirm` issued by the service provider.

   .. positive:: A service provider may issue a `Disconnect.indication` primitive on an established connection at any time.

.. question:: co-service2
   :nb_pos: 2
   :nb_prop: 4

   3. Consider the connection-oriented transport service. Among the following affirmations about this service, select the ones that are correct.

   .. positive:: With a message-mode service, each `Data.request` issued by one user will lead to a `Data.indication` at the other end.

   .. negative:: With a bytestream service, each `Data.request` issued by one user will lead to a `Data.indication` at the other end.

   .. positive:: A transport service provider may issue a `Disconnect.indication` at any time to terminate a connection.

   .. negative:: A transport service provider will only issue a `Disconnection.indication` after having received a `Disconnect.request` from the other user.

   .. positive:: An abrupt connection release may cause some SDUs to be discarded.

   .. negative:: An abrupt connection release may cause some SDUs to be corrupted.

   .. positive:: When a user issues a graceful `Disconnect.req`, only one direction of transfer is closed.

   .. negative:: A transport service provider may itself issue a `Disconnect.indication` to gracefully terminate a connection.

      .. comment:: A connection release issued by the provider is always an abrupt release.

   .. positive:: A user may issue a `Data.request` after having received a graceful `Disconnect.indication`

   .. negative:: A user may issue a `Data.request` after having issued a graceful `Disconnect.request`

   .. negative:: A transport service provider may issue a `Data.indication` primitive to a user after having received a graceful `Disconnect.request` from this user.


.. question:: networklayer
   :nb_prop: 3
   :nb_pos: 2

   4. Which of the following affirmations correspond to the behaviour of the network layer ? Select all the correct ones.

   .. positive:: The network layer may loose packets

   .. positive:: The network layer may modify the content of packets

   .. negative:: The network layer always deliver packets in sequence

   .. negative:: The network layer will never deliver a given packet twice

   .. positive:: The network layer may deliver the same packet several times to a given destination

.. question:: cltransport
   :nb_prop: 4
   :nb_pos: 2

   5. Which of the following mechanisms are likely to be used inside a protocol that provides the unreliable connectionless transport service running on top of an unreliable connectionless network layer. ? Select all the applicable mechanisms.

   .. positive:: A checksum to detect transmission errors.

      .. comment:: Even if the transport service is unreliable, applications usually do not want to receive corrupted data.

   .. positive:: A CRC to detect transmission errors.

      .. comment:: Even if the transport service is unreliable, applications usually do not want to receive corrupted data.

   .. positive:: Port numbers to identify the communicating applications.

   .. negative:: Sequence numbers to detect out-of-order data.

      .. comment:: If the transport service is unreliable, then there is not need to use sequence number to detect out-of-order data.

   .. negative:: A retransmission timer to retransmit lost data.

      .. comment:: If the transport service is unreliable, then there is no need to try to retransmit lost data.

   .. negative:: A connection establishment mechanism.

      .. comment:: This is required when providing the connection-oriented transport service, but not for a connectionless one.

   .. negative:: Go-back-n.

      .. comment:: A connectionless transport service provides an unreliable service. Go-bak-n is a technique to ensure the reliable delivery of data.

   .. negative:: Selective repeat.

      .. comment:: A connectionless transport service provides an unreliable service. Selective repeat is a technique to ensure the reliable delivery of data.

.. question:: twh1
   :nb_prop: 3
   :nb_pos: 1

   6. The three-way handshake allows to negotiate successfully the establishment of a transport connection. Among the following time-sequence diagrams, which is the one that corresponds to a valid three-way handshake ?

   .. positive::

      .. msc::

         a [label="", linecolour=white],
         b [label="Host A", linecolour=black],
         z [label="", linecolour=white],
         c [label="Host B", linecolour=black],
         d [label="", linecolour=white];
         a=>b [ label = "CONNECT.req()" ] ,
         b>>c [ label = "CR(seq=1341)", arcskip="1"];
         c=>d [ label = "CONNECT.ind()" ];
         d=>c [ label = "CONNECT.resp()" ],
         c>>b [ label = "CA(ack=1341,seq=2141)", arcskip="1"];
         b=>a [ label = "CONNECT.conf()" ]; 
         b>>c [ label = "CA(seq=1341,ack=2141)", arcskip="1"];
         |||;

   .. negative::

      .. msc::
  
         a [label="", linecolour=white],
         b [label="Host A", linecolour=black],
         z [label="", linecolour=white],
         c [label="Host B", linecolour=black],
         d [label="", linecolour=white];
         a=>b [ label = "CONNECT.req()" ] ,
         b>>c [ label = "CR(seq=1341)", arcskip="1"];
         c=>d [ label = "CONNECT.ind()" ];
         d=>c [ label = "CONNECT.resp()" ],
         c>>b [ label = "CA(ack=1,seq=2)", arcskip="1"];
         b=>a [ label = "CONNECT.conf()" ]; 
         b>>c [ label = "CA(seq=1,ack=2)", arcskip="1"];
         |||;

      .. comment:: This diagram is incorrect. `Host B` should reply with a `CR` segment that confirms the correction reception of `CR(seq=1341)`. This requires an acknowledgement for sequence number `1341`. The third `CA` segment is also incorrect.

   .. positive::

      .. msc::
  
         a [label="", linecolour=white],
         b [label="Host A", linecolour=black],
         z [label="", linecolour=white],
         c [label="Host B", linecolour=black],
         d [label="", linecolour=white];
         a=>b [ label = "CONNECT.req()" ] ,
         b>>c [ label = "CR(seq=2141)", arcskip="1"];
         c=>d [ label = "CONNECT.ind()" ];
         d=>c [ label = "CONNECT.resp()" ],
         c>>b [ label = "CA(ack=2141,seq=1341)", arcskip="1"];
         b=>a [ label = "CONNECT.conf()" ]; 
         b>>c [ label = "CA(seq=2141,ack=1341)", arcskip="1"];
         |||;

      .. comment:: This diagram is correct.

   .. negative::

      .. msc::
  
         a [label="", linecolour=white],
         b [label="Host A", linecolour=black],
         z [label="", linecolour=white],
         c [label="Host B", linecolour=black],
         d [label="", linecolour=white];
         a=>b [ label = "CONNECT.req()" ] ,
         b>>c [ label = "CR(seq=2141)", arcskip="1"];
         c=>d [ label = "CONNECT.ind()" ];
         d=>c [ label = "CONNECT.resp()" ],
         c>>b [ label = "CA(ack=1341,seq=2141)", arcskip="1"];
         b=>a [ label = "CONNECT.conf()" ];
         b>>c [ label = "CA(seq=2141,ack=2141)", arcskip="1"];
         |||;


      .. comment:: This diagram is incorrect. `Host B` should reply with a `CA` segment that confirms the correct reception of `CR(seq=2141)`. This requires an acknowledgement for sequence number `2141`. 


   .. negative::

      .. msc::

         a [label="", linecolour=white],
         b [label="Host A", linecolour=black],
         z [label="", linecolour=white],
         c [label="Host B", linecolour=black],
         d [label="", linecolour=white];
         a=>b [ label = "CONNECT.req()" ] ,
         b>>c [ label = "CR(seq=2141)", arcskip="1"];
         c=>d [ label = "CONNECT.ind()" ];
         d=>c [ label = "CONNECT.resp()" ],
         c>>b [ label = "CA(ack=2141,seq=1341)", arcskip="1"];
         b=>a [ label = "CONNECT.conf()" ];
         b>>c [ label = "CA(seq=2141,ack=2141)", arcskip="1"];
         |||;


      .. comment:: This diagram is incorrect. `Host A` should reply with a `CA` segment that confirms the correct reception of `CA(seq=1341,ack=2141)`. This requires an acknowledgement for sequence number `1341`. 


.. question:: twh2
   :nb_prop: 3
   :nb_pos: 1

   7. The three-way handshake allows to negotiate successfully the establishment of a transport connection. Consider a transport connection that begins which the exchange of two segments as shown in the figure below.

      .. msc::
  
         a [label="", linecolour=white],
         b [label="Host A", linecolour=black],
         z [label="", linecolour=white],
         c [label="Host B", linecolour=black],
         d [label="", linecolour=white];
         a=>b [ label = "CONNECT.req()" ] ,
         b>>c [ label = "CR(seq=12345)", arcskip="1"];
         c=>d [ label = "CONNECT.ind()" ];
         d=>c [ label = "CONNECT.resp()" ],
         c>>b [ label = "CA(seq=56789,ack=12345)", arcskip="1"];
         b=>a [ label = "CONNECT.conf()" ];
         |||;


   Consider what happens after the exchange of these two segments. Only one of the affirmations below is correct. Which one ? 

   .. positive:: If `Host B` receives `CR(seq=12345)`, it will respond with `CA(seq=56789,ack=12345)`

   .. positive:: If `Host B` does not receive `CA(seq=12345,ack=56789)` after some time, it will retransmit `CA(seq=56789,ack=12345)`.

   .. negative:: If `Host B` receives again `CR(seq=12345)`, it will discard the duplicate segment.

      .. comment:: This is incorrect. If `Host B` receives twice the same `CR` segment, this likely indicates that the first `CA` reply was lost and this needs to be retransmitted.

   .. negative:: If `Host B` receives again `CA(seq=56789,ack=12345)`, it will discard the duplicate segment.
      .. comment:: This is incorrect. If `Host A` receives twice the same `CA` segment, this likely indicates that the first `CA` reply that it sent was lost. The correction reaction is to retransmit the `CA` segment.

   .. negative:: At this stage, the connection is established and all `CA` segments that arrive should be considered as duplicate and discarded.

      .. comment:: This is incorrect. `Host A` needs to send `CA(seq=12345,ack=56789)` to confirm the establishment of the connection to `Host B`. If `Host B` does not receive this segment quickly enough, it will retransmit `CA(seq=56789,ack=12345)`.


.. include:: /links.rst
