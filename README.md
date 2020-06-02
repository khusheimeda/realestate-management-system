REAL ESTATE MANAGEMENT SYSTEM
The idea of this project is to have an online real estate management system, so that people can
easily buy and sell property 24x7. I will have an online portal where two types of users can

login-
1. Admin

2. Client
There are three types of property- land for sale, houses for sale, and any kind of building for
rent.
A client can register himself/herself on the online portal by giving his details. He can be a buyer
or a seller. If he is a seller, he will have to put up details of the property that he wishes to sell or
lease(in case of rental buildings). If he is a buyer, he can view the properties put up for sale by
querying the database for the kind of property he wants to buy(land/house/rental building) or
based on his price range, or based on location, etc.
Whenever a buyer decides to buy a property, he can book the property and the booking details
are stored in a separate table. Then he can make the payment for the property, all in one
transaction, or in parts. The payment details are stored in a separate table.
An admin does the job of overseeing the payments, and ensuring there is no discrepancy. A
minimum of 1 and a maximum of 5 admins are allowed.

Refer to dbms.txt for detailed procedure and explanation of relations and their attributes.
Refer to impl.txt for Postgresql statements, functions and triggers.

Backend DB used: Postgresql
Frontend done using: Flask, HTML, Bootstrap.
