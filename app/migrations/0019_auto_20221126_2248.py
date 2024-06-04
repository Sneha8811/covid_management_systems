# Generated by Django 2.2 on 2022-11-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20221126_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='city',
            field=models.CharField(blank=True, choices=[('Namakkal', 'Namakkal'), ('Dakshinakannada', 'Dakshinakannada'), ('Bharatpur', 'Bharatpur'), ('Ludhiana', 'Ludhiana'), ('Jhalawar', 'Jhalawar'), ('Sonepat', 'Sonepat'), ('Ujjire', 'Ujjire'), ('Koratty', 'Koratty'), ('Bijapur', 'Bijapur'), ('Pathanamthitta', 'Pathanamthitta'), ('Kanyakumari', 'Kanyakumari'), ('Gudivada', 'Gudivada'), ('Surat', 'Surat'), ('Kolkata', 'Kolkata'), ('Hubli', 'Hubli'), ('Nahan', 'Nahan'), ('Mumbai', 'Mumbai'), ('Aluva', 'Aluva'), ('Valapady', 'Valapady'), ('Kanchipuram', 'Kanchipuram'), ('Bhavnagar', 'Bhavnagar'), ('Idukki', 'Idukki'), ('Kurukshetra', 'Kurukshetra'), ('Hosur', 'Hosur'), ('Erode', 'Erode'), ('Jagatsinghapur', 'Jagatsinghapur'), ('Vizag', 'Vizag'), ('Ghaziabad', 'Ghaziabad'), ('Kolhapur', 'Kolhapur'), ('Kutch', 'Kutch'), ('Berhamapur', 'Berhamapur'), ('Vadodara', 'Vadodara'), ('Nanganallur', 'Nanganallur'), ('Pondicherry', 'Pondicherry'), ('Kadapa', 'Kadapa'), ('Surendranagar', 'Surendranagar'), ('Sindhudurga', 'Sindhudurga'), ('Kayamkulam', 'Kayamkulam'), ('Ernakulam', 'Ernakulam'), ('Karimnagar', 'Karimnagar'), ('Amraiwadi', 'Amraiwadi'), ('Sholapur', 'Sholapur'), ('Sagar', 'Sagar'), ('Aurangabad', 'Aurangabad'), ('Moradabad', 'Moradabad'), ('Bhatinda', 'Bhatinda'), ('Ratlam', 'Ratlam'), ('Ranbennur', 'Ranbennur'), ('North24Paraganas', 'North24Paraganas'), ('Tadepalligudam', 'Tadepalligudam'), ('Bangalore,', 'Bangalore,'), ('Visakhapatnam', 'Visakhapatnam'), ('Noida', 'Noida'), ('Salem', 'Salem'), ('Kanpur', 'Kanpur'), ('Krishnagiri', 'Krishnagiri'), ('Alleppey', 'Alleppey'), ('Khammam', 'Khammam'), ('Chellakere', 'Chellakere'), ('Navi Mumbai', 'Navi Mumbai'), ('Miryalaguda', 'Miryalaguda'), ('Secunderabad', 'Secunderabad'), ('Karur', 'Karur'), ('Dehradun', 'Dehradun'), ('Gurgaon', 'Gurgaon'), ('Bijnor', 'Bijnor'), ('Jalgaon', 'Jalgaon'), ('Tinsukia', 'Tinsukia'), ('Dibrugarh', 'Dibrugarh'), ('Badlapur', 'Badlapur'), ('Bhubaneswar', 'Bhubaneswar'), ('New Delhi', 'New Delhi'), ('Bikaner', 'Bikaner'), ('Garia', 'Garia'), ('Rajamundry', 'Rajamundry'), ('Kollam', 'Kollam'), ('Tumkur', 'Tumkur'), ('Kolar', 'Kolar'), ('Westgodavari', 'Westgodavari'), ('Gurdaspur', 'Gurdaspur'), ('Kurnool', 'Kurnool'), ('Wardha', 'Wardha'), ('Mehsana', 'Mehsana'), ('Cochin', 'Cochin'), ('Kundapur', 'Kundapur'), ('Chanapatna', 'Chanapatna'), ('Guwahati', 'Guwahati'), ('Chitradurga', 'Chitradurga'), ('Jamnagar', 'Jamnagar'), ('Ferozepur', 'Ferozepur'), ('Sriganganagar', 'Sriganganagar'), ('Gangavathi', 'Gangavathi'), ('Ranipat', 'Ranipat'), ('Godhra', 'Godhra'), ('Patan', 'Patan'), ('Tiruchirapalli', 'Tiruchirapalli'), ('Ramanagaram', 'Ramanagaram'), ('Trichur', 'Trichur'), ('Sivagangai', 'Sivagangai'), ('Karaikudi', 'Karaikudi'), ('Burdwan', 'Burdwan'), ('Madurai', 'Madurai'), ('Palakkad', 'Palakkad'), ('Azamgarh', 'Azamgarh'), ('Bantwal', 'Bantwal'), ('Channarayapatna', 'Channarayapatna'), ('Meerut', 'Meerut'), ('Jhansi', 'Jhansi'), ('Jammu', 'Jammu'), ('Virajpet', 'Virajpet'), ('Dindigul', 'Dindigul'), ('Gulbarga', 'Gulbarga'), ('Jabalpur', 'Jabalpur'), ('Ananthapur', 'Ananthapur'), ('Bhopal', 'Bhopal'), ('Solapur', 'Solapur'), ('Nagapattanam', 'Nagapattanam'), ('Kothagudem', 'Kothagudem'), ('Hapur', 'Hapur'), ('Tuticorin', 'Tuticorin'), ('Trichy', 'Trichy'), ('Dharmapuri', 'Dharmapuri'), ('Tirunelveli', 'Tirunelveli'), ('Theni', 'Theni'), ('Tiruppur', 'Tiruppur'), ('Mohali', 'Mohali'), ('Rangareddy', 'Rangareddy'), ('Kengeri Upanagara', 'Kengeri Upanagara'), ('Kannur', 'Kannur'), ('Karwar', 'Karwar'), ('Udupi', 'Udupi'), ('Gajuwaka', 'Gajuwaka'), ('Chengalpattu', 'Chengalpattu'), ('Anekal', 'Anekal'), ('Thiruvallur', 'Thiruvallur'), ('Tenali', 'Tenali'), ('Ahmedabad', 'Ahmedabad'), ('Srinagar', 'Srinagar'), ('Lucknow', 'Lucknow'), ('Kuzhithurai', 'Kuzhithurai'), ('Uran', 'Uran'), ('Koparkhairane', 'Koparkhairane'), ('Pune', 'Pune'), ('Scheme', 'Scheme'), ('Chittorgarh', 'Chittorgarh'), ('Wayanad', 'Wayanad'), ('Madanapalle', 'Madanapalle'), ('Rajkot', 'Rajkot'), ('Chikkaballapur', 'Chikkaballapur'), ('Jodhpur', 'Jodhpur'), ('Nalasopara', 'Nalasopara'), ('Patna', 'Patna'), ('Bidar', 'Bidar'), ('Jind', 'Jind'), ('Sambalpur', 'Sambalpur'), ('Dhenkanal', 'Dhenkanal'), ('Rohtak', 'Rohtak'), ('Krishna', 'Krishna'), ('Kumbakonam', 'Kumbakonam'), ('Mysore', 'Mysore'), ('Chennai', 'Chennai'), ('Chittoor', 'Chittoor'), ('Bhilai', 'Bhilai'), ('Kota', 'Kota'), ('Nadiad', 'Nadiad'), ('Cuttack', 'Cuttack'), ('Ranchi', 'Ranchi'), ('Amritsar', 'Amritsar'), ('Thane', 'Thane'), ('Raichur', 'Raichur'), ('Bargarh', 'Bargarh'), ('Puttur', 'Puttur'), ('Gwalior', 'Gwalior'), ('Shamshabad', 'Shamshabad'), ('Udaipur', 'Udaipur'), ('Amravati', 'Amravati'), ('Agra', 'Agra'), ('Nashik', 'Nashik'), ('Rewari', 'Rewari'), ('Nainital', 'Nainital'), ('Nalgonda', 'Nalgonda'), ('Vaishali', 'Vaishali'), ('Hardwar', 'Hardwar'), ('Trivandrum', 'Trivandrum'), ('Alwar', 'Alwar'), ('Panjim', 'Panjim'), ('Indore', 'Indore'), ('Warangal', 'Warangal'), ('Cuddalore', 'Cuddalore'), ('Kunnamkulam', 'Kunnamkulam'), ('Kukatpally', 'Kukatpally'), ('Mangalore', 'Mangalore'), ('Titagarh', 'Titagarh'), ('Mulbagal', 'Mulbagal'), ('Margao', 'Margao'), ('Baramati', 'Baramati'), ('Bellary', 'Bellary'), ('Dhanbad', 'Dhanbad'), ('Jallandhar', 'Jallandhar'), ('Nagpur', 'Nagpur'), ('Bareilly', 'Bareilly'), ('Villupuram', 'Villupuram'), ('Karnal', 'Karnal'), ('Khurda', 'Khurda'), ('Mandya', 'Mandya'), ('Delhi', 'Delhi'), ('Eluru', 'Eluru'), ('Jamkhed', 'Jamkhed'), ('Vijayawada', 'Vijayawada'), ('Nellore', 'Nellore'), ('Muktsar', 'Muktsar'), ('Guttahalli', 'Guttahalli'), ('Hassan', 'Hassan'), ('Durg', 'Durg'), ('Panchkula', 'Panchkula'), ('Sonitpur', 'Sonitpur'), ('Aligarh', 'Aligarh'), ('Jaipur', 'Jaipur'), ('Siliguri', 'Siliguri'), ('Malapuram', 'Malapuram'), ('Buldana', 'Buldana'), ('Raipur', 'Raipur'), ('Machlipatanam', 'Machlipatanam'), ('Sangli', 'Sangli'), ('Gandhinagar', 'Gandhinagar'), ('Nangloi', 'Nangloi'), ('Haldwani', 'Haldwani'), ('Tanjore', 'Tanjore'), ('Kundalahalli', 'Kundalahalli'), ('Guntur', 'Guntur'), ('Tiruchendur', 'Tiruchendur'), ('Patiala', 'Patiala'), ('Coimbatore', 'Coimbatore'), ('Panipat', 'Panipat'), ('Rajahmundry', 'Rajahmundry'), ('Baroda', 'Baroda'), ('Eastgodavari', 'Eastgodavari'), ('Ahmednagar', 'Ahmednagar'), ('Hooghly', 'Hooghly'), ('Malegaon', 'Malegaon'), ('Varanasi', 'Varanasi'), ('Hsr Layout', 'Hsr Layout'), ('Kullu', 'Kullu'), ('Hissar', 'Hissar'), ('Kadur', 'Kadur'), ('Raigad', 'Raigad'), ('Ulhasnagar', 'Ulhasnagar'), ('Kendrapada', 'Kendrapada'), ('Chickmangalur', 'Chickmangalur'), ('Bagalkot', 'Bagalkot'), ('Virudhunagar', 'Virudhunagar'), ('Sangamner', 'Sangamner'), ('Jhajjar', 'Jhajjar'), ('Parbhani', 'Parbhani'), ('Tirupur', 'Tirupur'), ('Kozhicode', 'Kozhicode'), ('Bilaspur', 'Bilaspur'), ('Belthangady', 'Belthangady'), ('Belgaum', 'Belgaum'), ('Calicut', 'Calicut'), ('Kasaragod', 'Kasaragod'), ('Himayatnagar', 'Himayatnagar'), ('Ballabgarh', 'Ballabgarh'), ('Ashok Nagar', 'Ashok Nagar'), ('Bankura', 'Bankura'), ('Ajmer', 'Ajmer'), ('Sivakasi', 'Sivakasi'), ('Thrissur', 'Thrissur'), ('Hyderabad', 'Hyderabad'), ('Ongole', 'Ongole'), ('Porbandar', 'Porbandar'), ('Bhiwandi', 'Bhiwandi'), ('Howrah', 'Howrah'), ('Allahabad', 'Allahabad'), ('Mira Road', 'Mira Road'), ('Bhadravathi', 'Bhadravathi'), ('Ankola', 'Ankola'), ('Bhosari', 'Bhosari'), ('Shimoga', 'Shimoga'), ('Manacaud', 'Manacaud'), ('Nagarbhavi', 'Nagarbhavi'), ('Kumta', 'Kumta'), ('Kheda', 'Kheda'), ('Bharuch', 'Bharuch'), ('Bangalore', 'Bangalore'), ('Kottayam', 'Kottayam'), ('Faridabad', 'Faridabad'), ('Sangrur', 'Sangrur'), ('Korba', 'Korba'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Ratnagiri', 'Ratnagiri'), ('Nagercoil', 'Nagercoil'), ('Chandigarh', 'Chandigarh'), ('Pollachi', 'Pollachi'), ('Dewas', 'Dewas'), ('Davangere', 'Davangere'), ('Barnala', 'Barnala'), ('Ambala', 'Ambala')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admission',
            name='state',
            field=models.CharField(blank=True, choices=[('Chattisgarh', 'Chattisgarh'), ('Jharkhand', 'Jharkhand'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Tamilnadu', 'Tamilnadu'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Haryana', 'Haryana'), ('Rajasthan', 'Rajasthan'), ('Assam', 'Assam'), ('Kerala', 'Kerala'), ('Punjab', 'Punjab'), ('Goa', 'Goa'), ('Orissa', 'Orissa'), ('Uttaranchal', 'Uttaranchal'), ('Karnataka', 'Karnataka'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Gujarat', 'Gujarat'), ('Uttarakhand', 'Uttarakhand'), ('Bihar', 'Bihar'), ('West Bengal', 'West Bengal'), ('Delhi', 'Delhi'), ('Maharashtra', 'Maharashtra')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='carecenterpatientdetails',
            name='bed_type',
            field=models.CharField(blank=True, default='Without oxygen', max_length=20, null=True),
        ),
    ]