# Generated by Django 2.2 on 2022-11-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_auto_20221127_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='city',
            field=models.CharField(blank=True, choices=[('Bhubaneswar', 'Bhubaneswar'), ('Trichy', 'Trichy'), ('Sambalpur', 'Sambalpur'), ('Ajmer', 'Ajmer'), ('Sriganganagar', 'Sriganganagar'), ('Jhansi', 'Jhansi'), ('Mysore', 'Mysore'), ('Chitradurga', 'Chitradurga'), ('Kundalahalli', 'Kundalahalli'), ('Mira Road', 'Mira Road'), ('Mumbai', 'Mumbai'), ('Chellakere', 'Chellakere'), ('Bidar', 'Bidar'), ('Ferozepur', 'Ferozepur'), ('Nangloi', 'Nangloi'), ('Chennai', 'Chennai'), ('Ujjire', 'Ujjire'), ('Eastgodavari', 'Eastgodavari'), ('Madanapalle', 'Madanapalle'), ('Kheda', 'Kheda'), ('Karwar', 'Karwar'), ('Srinagar', 'Srinagar'), ('Krishnagiri', 'Krishnagiri'), ('Parbhani', 'Parbhani'), ('Hsr Layout', 'Hsr Layout'), ('Dhenkanal', 'Dhenkanal'), ('Bijnor', 'Bijnor'), ('Kumbakonam', 'Kumbakonam'), ('Bareilly', 'Bareilly'), ('Tumkur', 'Tumkur'), ('Erode', 'Erode'), ('Kurukshetra', 'Kurukshetra'), ('Gajuwaka', 'Gajuwaka'), ('Bankura', 'Bankura'), ('Patiala', 'Patiala'), ('Sholapur', 'Sholapur'), ('Karnal', 'Karnal'), ('Jodhpur', 'Jodhpur'), ('Koparkhairane', 'Koparkhairane'), ('Thane', 'Thane'), ('Guttahalli', 'Guttahalli'), ('Ballabgarh', 'Ballabgarh'), ('Jagatsinghapur', 'Jagatsinghapur'), ('Kozhicode', 'Kozhicode'), ('Belthangady', 'Belthangady'), ('Buldana', 'Buldana'), ('Thiruvallur', 'Thiruvallur'), ('Chandigarh', 'Chandigarh'), ('Channarayapatna', 'Channarayapatna'), ('Kottayam', 'Kottayam'), ('Salem', 'Salem'), ('Gandhinagar', 'Gandhinagar'), ('Wardha', 'Wardha'), ('Manacaud', 'Manacaud'), ('Jallandhar', 'Jallandhar'), ('Hissar', 'Hissar'), ('Dehradun', 'Dehradun'), ('Kannur', 'Kannur'), ('Koratty', 'Koratty'), ('North24Paraganas', 'North24Paraganas'), ('Eluru', 'Eluru'), ('Ambala', 'Ambala'), ('Ratnagiri', 'Ratnagiri'), ('Kadapa', 'Kadapa'), ('Khammam', 'Khammam'), ('Rajkot', 'Rajkot'), ('Ernakulam', 'Ernakulam'), ('Tirupur', 'Tirupur'), ('Ashok Nagar', 'Ashok Nagar'), ('Villupuram', 'Villupuram'), ('Scheme', 'Scheme'), ('Rohtak', 'Rohtak'), ('Miryalaguda', 'Miryalaguda'), ('Tiruchirapalli', 'Tiruchirapalli'), ('Dibrugarh', 'Dibrugarh'), ('Kutch', 'Kutch'), ('Kasaragod', 'Kasaragod'), ('Bhopal', 'Bhopal'), ('Dharmapuri', 'Dharmapuri'), ('Vizag', 'Vizag'), ('Ongole', 'Ongole'), ('Rewari', 'Rewari'), ('Bangalore,', 'Bangalore,'), ('Godhra', 'Godhra'), ('Sangamner', 'Sangamner'), ('Jhalawar', 'Jhalawar'), ('Bellary', 'Bellary'), ('Titagarh', 'Titagarh'), ('Siliguri', 'Siliguri'), ('Secunderabad', 'Secunderabad'), ('Chengalpattu', 'Chengalpattu'), ('Moradabad', 'Moradabad'), ('Nagarbhavi', 'Nagarbhavi'), ('Gulbarga', 'Gulbarga'), ('Tinsukia', 'Tinsukia'), ('Ghaziabad', 'Ghaziabad'), ('Ramanagaram', 'Ramanagaram'), ('Bharatpur', 'Bharatpur'), ('Jamnagar', 'Jamnagar'), ('Hooghly', 'Hooghly'), ('Howrah', 'Howrah'), ('Tirunelveli', 'Tirunelveli'), ('Ludhiana', 'Ludhiana'), ('Dewas', 'Dewas'), ('Vadodara', 'Vadodara'), ('Sivakasi', 'Sivakasi'), ('Surendranagar', 'Surendranagar'), ('Udaipur', 'Udaipur'), ('Wayanad', 'Wayanad'), ('Amritsar', 'Amritsar'), ('Visakhapatnam', 'Visakhapatnam'), ('Chittorgarh', 'Chittorgarh'), ('Sonitpur', 'Sonitpur'), ('Machlipatanam', 'Machlipatanam'), ('Anekal', 'Anekal'), ('Bikaner', 'Bikaner'), ('Porbandar', 'Porbandar'), ('Chanapatna', 'Chanapatna'), ('Hyderabad', 'Hyderabad'), ('Belgaum', 'Belgaum'), ('Mulbagal', 'Mulbagal'), ('Ranipat', 'Ranipat'), ('Guntur', 'Guntur'), ('Pollachi', 'Pollachi'), ('Westgodavari', 'Westgodavari'), ('Mandya', 'Mandya'), ('Ahmednagar', 'Ahmednagar'), ('Virajpet', 'Virajpet'), ('Gangavathi', 'Gangavathi'), ('Hosur', 'Hosur'), ('Nellore', 'Nellore'), ('Sonepat', 'Sonepat'), ('Tuticorin', 'Tuticorin'), ('Tanjore', 'Tanjore'), ('Nagpur', 'Nagpur'), ('Kota', 'Kota'), ('Raichur', 'Raichur'), ('Chickmangalur', 'Chickmangalur'), ('Kadur', 'Kadur'), ('Hapur', 'Hapur'), ('Korba', 'Korba'), ('Kuzhithurai', 'Kuzhithurai'), ('Sangli', 'Sangli'), ('Ratlam', 'Ratlam'), ('Hubli', 'Hubli'), ('Sagar', 'Sagar'), ('Jind', 'Jind'), ('Dakshinakannada', 'Dakshinakannada'), ('Trichur', 'Trichur'), ('Baroda', 'Baroda'), ('Cochin', 'Cochin'), ('Coimbatore', 'Coimbatore'), ('Azamgarh', 'Azamgarh'), ('Shimoga', 'Shimoga'), ('Bilaspur', 'Bilaspur'), ('Varanasi', 'Varanasi'), ('Bargarh', 'Bargarh'), ('Bijapur', 'Bijapur'), ('Nainital', 'Nainital'), ('Cuttack', 'Cuttack'), ('Gudivada', 'Gudivada'), ('Indore', 'Indore'), ('Bharuch', 'Bharuch'), ('New Delhi', 'New Delhi'), ('Bhadravathi', 'Bhadravathi'), ('Davangere', 'Davangere'), ('Surat', 'Surat'), ('Bantwal', 'Bantwal'), ('Guwahati', 'Guwahati'), ('Lucknow', 'Lucknow'), ('Tiruchendur', 'Tiruchendur'), ('Dhanbad', 'Dhanbad'), ('Kengeri Upanagara', 'Kengeri Upanagara'), ('Haldwani', 'Haldwani'), ('Theni', 'Theni'), ('Rajamundry', 'Rajamundry'), ('Madurai', 'Madurai'), ('Kolkata', 'Kolkata'), ('Amraiwadi', 'Amraiwadi'), ('Aurangabad', 'Aurangabad'), ('Sivagangai', 'Sivagangai'), ('Puttur', 'Puttur'), ('Udupi', 'Udupi'), ('Trivandrum', 'Trivandrum'), ('Mohali', 'Mohali'), ('Panipat', 'Panipat'), ('Muktsar', 'Muktsar'), ('Nadiad', 'Nadiad'), ('Malapuram', 'Malapuram'), ('Kanyakumari', 'Kanyakumari'), ('Raipur', 'Raipur'), ('Mehsana', 'Mehsana'), ('Namakkal', 'Namakkal'), ('Durg', 'Durg'), ('Karimnagar', 'Karimnagar'), ('Alleppey', 'Alleppey'), ('Idukki', 'Idukki'), ('Burdwan', 'Burdwan'), ('Meerut', 'Meerut'), ('Nanganallur', 'Nanganallur'), ('Gurgaon', 'Gurgaon'), ('Berhamapur', 'Berhamapur'), ('Bangalore', 'Bangalore'), ('Kendrapada', 'Kendrapada'), ('Valapady', 'Valapady'), ('Sindhudurga', 'Sindhudurga'), ('Rajahmundry', 'Rajahmundry'), ('Malegaon', 'Malegaon'), ('Jhajjar', 'Jhajjar'), ('Alwar', 'Alwar'), ('Thrissur', 'Thrissur'), ('Calicut', 'Calicut'), ('Jalgaon', 'Jalgaon'), ('Gurdaspur', 'Gurdaspur'), ('Bhavnagar', 'Bhavnagar'), ('Chittoor', 'Chittoor'), ('Kundapur', 'Kundapur'), ('Faridabad', 'Faridabad'), ('Jabalpur', 'Jabalpur'), ('Karaikudi', 'Karaikudi'), ('Vaishali', 'Vaishali'), ('Barnala', 'Barnala'), ('Mangalore', 'Mangalore'), ('Shamshabad', 'Shamshabad'), ('Aluva', 'Aluva'), ('Badlapur', 'Badlapur'), ('Bhiwandi', 'Bhiwandi'), ('Kurnool', 'Kurnool'), ('Aligarh', 'Aligarh'), ('Nagercoil', 'Nagercoil'), ('Solapur', 'Solapur'), ('Chikkaballapur', 'Chikkaballapur'), ('Pathanamthitta', 'Pathanamthitta'), ('Karur', 'Karur'), ('Gwalior', 'Gwalior'), ('Kollam', 'Kollam'), ('Hardwar', 'Hardwar'), ('Kolhapur', 'Kolhapur'), ('Tenali', 'Tenali'), ('Panchkula', 'Panchkula'), ('Himayatnagar', 'Himayatnagar'), ('Kullu', 'Kullu'), ('Cuddalore', 'Cuddalore'), ('Ulhasnagar', 'Ulhasnagar'), ('Kukatpally', 'Kukatpally'), ('Raigad', 'Raigad'), ('Nagapattanam', 'Nagapattanam'), ('Warangal', 'Warangal'), ('Ankola', 'Ankola'), ('Patna', 'Patna'), ('Agra', 'Agra'), ('Garia', 'Garia'), ('Kanchipuram', 'Kanchipuram'), ('Ranbennur', 'Ranbennur'), ('Kothagudem', 'Kothagudem'), ('Virudhunagar', 'Virudhunagar'), ('Panjim', 'Panjim'), ('Bagalkot', 'Bagalkot'), ('Pune', 'Pune'), ('Uran', 'Uran'), ('Kayamkulam', 'Kayamkulam'), ('Navi Mumbai', 'Navi Mumbai'), ('Jammu', 'Jammu'), ('Sangrur', 'Sangrur'), ('Rangareddy', 'Rangareddy'), ('Pondicherry', 'Pondicherry'), ('Palakkad', 'Palakkad'), ('Hassan', 'Hassan'), ('Tadepalligudam', 'Tadepalligudam'), ('Bhilai', 'Bhilai'), ('Amravati', 'Amravati'), ('Tiruppur', 'Tiruppur'), ('Nahan', 'Nahan'), ('Allahabad', 'Allahabad'), ('Patan', 'Patan'), ('Bhosari', 'Bhosari'), ('Noida', 'Noida'), ('Kanpur', 'Kanpur'), ('Margao', 'Margao'), ('Ahmedabad', 'Ahmedabad'), ('Ananthapur', 'Ananthapur'), ('Baramati', 'Baramati'), ('Nalasopara', 'Nalasopara'), ('Delhi', 'Delhi'), ('Kumta', 'Kumta'), ('Jaipur', 'Jaipur'), ('Bhatinda', 'Bhatinda'), ('Dindigul', 'Dindigul'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Kunnamkulam', 'Kunnamkulam'), ('Vijayawada', 'Vijayawada'), ('Jamkhed', 'Jamkhed'), ('Nashik', 'Nashik'), ('Ranchi', 'Ranchi'), ('Khurda', 'Khurda'), ('Nalgonda', 'Nalgonda'), ('Kolar', 'Kolar'), ('Krishna', 'Krishna')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admission',
            name='state',
            field=models.CharField(blank=True, choices=[('Goa', 'Goa'), ('Uttarakhand', 'Uttarakhand'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Kerala', 'Kerala'), ('Haryana', 'Haryana'), ('Jharkhand', 'Jharkhand'), ('Punjab', 'Punjab'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Karnataka', 'Karnataka'), ('West Bengal', 'West Bengal'), ('Gujarat', 'Gujarat'), ('Tamilnadu', 'Tamilnadu'), ('Orissa', 'Orissa'), ('Chattisgarh', 'Chattisgarh'), ('Uttaranchal', 'Uttaranchal'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Delhi', 'Delhi'), ('Maharashtra', 'Maharashtra'), ('Rajasthan', 'Rajasthan'), ('Bihar', 'Bihar'), ('Assam', 'Assam')], default=None, max_length=100, null=True),
        ),
    ]
