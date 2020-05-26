insert into Admin values('a1', 'a1');
insert into Admin values('a2', 'new');
insert into Admin values('a3', 'abc');

insert into Client_Address values('560102', 'Bangalore', 'Karnataka');
insert into Client_Address values('560063', 'Bangalore', 'Karnataka');	
insert into Client_Address values('560034', 'Bangalore', 'Karnataka');	
insert into Client_Address values('560085', 'Bangalore', 'Karnataka');	
insert into Client_Address values('560038', 'Bangalore', 'Karnataka');	
insert into Client_Address values('560078', 'Bangalore', 'Karnataka');	
insert into Client_Address values('560037', 'Bangalore', 'Karnataka');	
insert into Client_Address values('560003', 'Bangalore', 'Karnataka');	
insert into Client_Address values('500004', 'Hyderabad', 'Telangana');	
insert into Client_Address values('500013', 'Hyderabad', 'Telangana');	
insert into Client_Address values('500034', 'Hyderabad', 'Telangana');	
insert into Client_Address values('400053', 'Mumbai', 'Maharashtra');	
insert into Client_Address values('400050' , 'Mumbai', 'Maharashtra');	
insert into Client_Address values('400091', 'Mumbai', 'Maharashtra');	
insert into Client_Address values('400062', 'Mumbai', 'Maharashtra');	
insert into Client_Address values('583114', 'Bellary', 'Karnataka');	
insert into Client_Address values('571302', 'Mysore', 'Karnataka');	
insert into Client_Address values('571102', 'Mysore', 'Karnataka');	


insert into Client values('C1','Anu','7259939624','2000-06-08', '123456789011', '560102');
insert into Client values('C2','Arun','7259939625','1999-06-08', '123456789101', '400050');
insert into Client values('C3','Roy','9876543210','1979-12-10', NULL, '500034');
insert into Client values('C4','Sam','8251959025','2002-01-15', NULL, '571102');
insert into Client values('C5','Vishnu','9448466723','1939-05-01', '354126519884', '560037');
insert into Client values('C6','Meghana','9731555782','1972-12-30', '432187650987', '400050');
insert into Client values('C7','Natasha','9731222896','2000-07-09', '909050502020', '560102');
insert into Client values('C8','Karthik','8143460891','1998-04-23', '532187650987', '560078');
insert into Client values('C9','Arjun','7258838624','1991-01-18', '912345789190', '400091');
insert into Client values('C10','Varun','8159939625','1980-11-11', '123456389101', '583114');


insert into Property values('L1','Land', 'C1','2020-05-24', 'Unsold');
insert into Property values('L2','Land', 'C1','2019-12-12', 'Booked');
insert into Property values('L3','Land', 'C6','2020-02-13', 'Sold');
insert into Property values('L4','Land', 'C8','2020-04-23', 'Booked');
insert into Property values('L5','Land', 'C7','2020-05-24', 'Unsold');
insert into Property values('H1','House', 'C5','2020-01-30', 'Unsold');
insert into Property values('H2','House', 'C9','2020-05-24', 'Unsold');
insert into Property values('H3','House', 'C9','2020-01-01', 'Booked');
insert into Property values('H4','House', 'C1','2019-09-15', 'Sold');
insert into Property values('H5','House', 'C6','2020-03-02', 'Unsold');
insert into Property values('R1','Rent', 'C10','2020-05-01', 'Unsold');
insert into Property values('R2','Rent', 'C10','2020-05-01', 'Booked');
insert into Property values('R3','Rent', 'C5','2019-11-28', 'Unsold');
insert into Property values('R4','Rent', 'C1','2020-01-11', 'Sold');
insert into Property values('R5','Rent', 'C1','2020-01-13', 'Unsold');

insert into Land values('L1', '171', '18th Main', 'HSR Layout', 'Bangalore', 'Karnataka', '560102', 30, 40, 'West', 1000000);
insert into Land values('L2', '120', '22nd Cross', 'Koramangala', 'Bangalore', 'Karnataka', '560034', 50, 40, 'South', 2000000);
insert into Land values('L3', '1108', '3rd Cross', 'JP Nagar', 'Bangalore', 'Karnataka', '560078', 80, 60, 'East', 10000000);
insert into Land values('L4', '20', '14th Main', 'Borevali', 'Mumbai', 'Maharashtra', '400091', 20, 30, 'West', 1000000);
insert into Land values('L5', '365', '19th Main', 'HSR Layout', 'Bangalore', 'Karnataka', '560102', 60, 40, 'West', 2500000);

insert into House values('H1', '1','10th Cross', 'Goregaon', 'Mumbai', 'Maharashtra', '400062', 'East', 2, '0', 15000000);
insert into House values('H2', '2','11th Cross', 'Debur', 'Mysore', 'Karnataka', '571302', 'North', 3, '1', 15000000);
insert into House values('H3', '3','12th Cross', 'Koramangala', 'Bangalore', 'Karnataka', '560034', 'South', 1, '0', 8000000);
insert into House values('H4', '4','13th Cross', 'Banjara Hills', 'Hyderabad', 'Telangana', '500034', 'South', 3, '1', 20000000);
insert into House values('H5', '5','14th Cross', 'Amberpet', 'Hyderbad', 'Telangana', '500013', 'West', 2, '0', 10000000);

insert into Rent values('R1', '501', '3rd Main', 'Gorahalli', 'Mysore', 'Karnataka', '571102', 'South', 3, '1', 'Family', 30000,300000);
insert into Rent values('R2', '502', '3rd Main', 'Gorahalli', 'Mysore', 'Karnataka', '571102', 'South', 1, '0', 'Bachelor', 5000,50000);
insert into Rent values('R3', '503', '4th Main', 'Koramangala', 'Bangalore', 'Karnataka', '560034', 'West', 3, '1', 'Corporate', 50000,500000);
insert into Rent values('R4', '504', '5th Main', 'HSR Layout', 'Bangalore', 'Karnataka', '560102', 'East', 3, '1', 'Corporate', 40000,400000);
insert into Rent values('R5', '505', '6th Main', 'HSR Layout', 'Bangalore', 'Karnataka', '570102', 'East', 2, '0', 'Bachelor', 12000,120000);
 
insert into Book values('B1', '2020-01-15', 'L2', 'C1', 'C3');
insert into Book values('B2', '2020-05-02', 'L4', 'C8', 'C2');
insert into Book values('B3', '2020-01-30', 'H3', 'C9', 'C1');
insert into Book values('B4', '2020-05-15', 'R2', 'C10', 'C3');
insert into Book values('B5', '2020-02-21', 'L3', 'C6', 'C4');
insert into Book values('B6', '2019-10-21', 'H4', 'C1', 'C8');
insert into Book values('B7', '2020-02-16', 'R4', 'C1', 'C5');

insert into Payment values('PAY1', '1111111111', 'Partially Paid', 'B1', 'C3');
insert into Payment values('PAY2', '2222222222', 'Partially Paid', 'B2', 'C2');
insert into Payment values('PAY3', '3333333333', 'Partially Paid', 'B3', 'C1');
insert into Payment values('PAY4', '4444444444', 'Partially Paid', 'B4', 'C3');
insert into Payment values('PAY5', '1111100000', 'Fully Paid', 'B5', 'C4');
insert into Payment values('PAY6', '1111100001', 'Fully Paid', 'B6', 'C8');
insert into Payment values('PAY7', '1111100002', 'Fully Paid', 'B7', 'C5');

