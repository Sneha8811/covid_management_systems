# Generated by Django 2.2 on 2022-11-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20221126_2332'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbookedadmissionhistory',
            name='admission_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='admission',
            name='city',
            field=models.CharField(blank=True, choices=[('Eastgodavari', 'Eastgodavari'), ('Gajuwaka', 'Gajuwaka'), ('Mandya', 'Mandya'), ('Meerut', 'Meerut'), ('Amritsar', 'Amritsar'), ('Bhilai', 'Bhilai'), ('Davangere', 'Davangere'), ('Ambala', 'Ambala'), ('Chitradurga', 'Chitradurga'), ('Khammam', 'Khammam'), ('Ajmer', 'Ajmer'), ('Kendrapada', 'Kendrapada'), ('Kumta', 'Kumta'), ('Nashik', 'Nashik'), ('Trivandrum', 'Trivandrum'), ('Karaikudi', 'Karaikudi'), ('Bantwal', 'Bantwal'), ('Jhajjar', 'Jhajjar'), ('Mysore', 'Mysore'), ('Chennai', 'Chennai'), ('Kurnool', 'Kurnool'), ('Kundapur', 'Kundapur'), ('Raipur', 'Raipur'), ('Tenali', 'Tenali'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Virajpet', 'Virajpet'), ('Bharuch', 'Bharuch'), ('Kundalahalli', 'Kundalahalli'), ('Bareilly', 'Bareilly'), ('Kheda', 'Kheda'), ('Kolhapur', 'Kolhapur'), ('Guwahati', 'Guwahati'), ('Rangareddy', 'Rangareddy'), ('Karnal', 'Karnal'), ('Hardwar', 'Hardwar'), ('Thrissur', 'Thrissur'), ('Jhansi', 'Jhansi'), ('Ulhasnagar', 'Ulhasnagar'), ('Dindigul', 'Dindigul'), ('New Delhi', 'New Delhi'), ('Chengalpattu', 'Chengalpattu'), ('Kullu', 'Kullu'), ('Chittoor', 'Chittoor'), ('Lucknow', 'Lucknow'), ('Cuttack', 'Cuttack'), ('Koparkhairane', 'Koparkhairane'), ('Guttahalli', 'Guttahalli'), ('Sivagangai', 'Sivagangai'), ('Ahmednagar', 'Ahmednagar'), ('Hassan', 'Hassan'), ('Jodhpur', 'Jodhpur'), ('Malapuram', 'Malapuram'), ('Pollachi', 'Pollachi'), ('Navi Mumbai', 'Navi Mumbai'), ('Gurdaspur', 'Gurdaspur'), ('Ernakulam', 'Ernakulam'), ('Jallandhar', 'Jallandhar'), ('Bankura', 'Bankura'), ('Bikaner', 'Bikaner'), ('Sangamner', 'Sangamner'), ('North24Paraganas', 'North24Paraganas'), ('Kadapa', 'Kadapa'), ('Gulbarga', 'Gulbarga'), ('Theni', 'Theni'), ('Salem', 'Salem'), ('Hyderabad', 'Hyderabad'), ('Alleppey', 'Alleppey'), ('Bijapur', 'Bijapur'), ('Hsr Layout', 'Hsr Layout'), ('Bijnor', 'Bijnor'), ('Kannur', 'Kannur'), ('Madurai', 'Madurai'), ('Kadur', 'Kadur'), ('Jamnagar', 'Jamnagar'), ('Surendranagar', 'Surendranagar'), ('Namakkal', 'Namakkal'), ('Chandigarh', 'Chandigarh'), ('Nanganallur', 'Nanganallur'), ('Surat', 'Surat'), ('Puttur', 'Puttur'), ('Ankola', 'Ankola'), ('Dhanbad', 'Dhanbad'), ('Bhadravathi', 'Bhadravathi'), ('Azamgarh', 'Azamgarh'), ('Baramati', 'Baramati'), ('Jamkhed', 'Jamkhed'), ('Patna', 'Patna'), ('Tiruchirapalli', 'Tiruchirapalli'), ('Tirupur', 'Tirupur'), ('Hosur', 'Hosur'), ('Jaipur', 'Jaipur'), ('Sholapur', 'Sholapur'), ('Villupuram', 'Villupuram'), ('Ghaziabad', 'Ghaziabad'), ('Agra', 'Agra'), ('Madanapalle', 'Madanapalle'), ('Badlapur', 'Badlapur'), ('Bangalore', 'Bangalore'), ('Aligarh', 'Aligarh'), ('Visakhapatnam', 'Visakhapatnam'), ('Rajahmundry', 'Rajahmundry'), ('Gwalior', 'Gwalior'), ('Nalgonda', 'Nalgonda'), ('Tinsukia', 'Tinsukia'), ('Dibrugarh', 'Dibrugarh'), ('Dewas', 'Dewas'), ('Chickmangalur', 'Chickmangalur'), ('Durg', 'Durg'), ('Ratnagiri', 'Ratnagiri'), ('Sangrur', 'Sangrur'), ('Patiala', 'Patiala'), ('Channarayapatna', 'Channarayapatna'), ('Warangal', 'Warangal'), ('Nalasopara', 'Nalasopara'), ('Dakshinakannada', 'Dakshinakannada'), ('Buldana', 'Buldana'), ('Kayamkulam', 'Kayamkulam'), ('Sagar', 'Sagar'), ('Ratlam', 'Ratlam'), ('Berhamapur', 'Berhamapur'), ('Ranchi', 'Ranchi'), ('Bhatinda', 'Bhatinda'), ('Ongole', 'Ongole'), ('Karwar', 'Karwar'), ('Sivakasi', 'Sivakasi'), ('Raigad', 'Raigad'), ('Chellakere', 'Chellakere'), ('Aurangabad', 'Aurangabad'), ('Muktsar', 'Muktsar'), ('Mumbai', 'Mumbai'), ('Gurgaon', 'Gurgaon'), ('Porbandar', 'Porbandar'), ('Nagercoil', 'Nagercoil'), ('Sambalpur', 'Sambalpur'), ('Himayatnagar', 'Himayatnagar'), ('Garia', 'Garia'), ('Bhiwandi', 'Bhiwandi'), ('Ahmedabad', 'Ahmedabad'), ('Panipat', 'Panipat'), ('Bidar', 'Bidar'), ('Machlipatanam', 'Machlipatanam'), ('Jagatsinghapur', 'Jagatsinghapur'), ('Indore', 'Indore'), ('Burdwan', 'Burdwan'), ('Uran', 'Uran'), ('Kukatpally', 'Kukatpally'), ('Vadodara', 'Vadodara'), ('Korba', 'Korba'), ('Trichur', 'Trichur'), ('Siliguri', 'Siliguri'), ('Secunderabad', 'Secunderabad'), ('Rohtak', 'Rohtak'), ('Ferozepur', 'Ferozepur'), ('Sriganganagar', 'Sriganganagar'), ('Coimbatore', 'Coimbatore'), ('Belgaum', 'Belgaum'), ('Hissar', 'Hissar'), ('Scheme', 'Scheme'), ('Sangli', 'Sangli'), ('Noida', 'Noida'), ('Bargarh', 'Bargarh'), ('Kasaragod', 'Kasaragod'), ('Udupi', 'Udupi'), ('Kota', 'Kota'), ('Allahabad', 'Allahabad'), ('Virudhunagar', 'Virudhunagar'), ('Dehradun', 'Dehradun'), ('Koratty', 'Koratty'), ('Mulbagal', 'Mulbagal'), ('Jhalawar', 'Jhalawar'), ('Kolar', 'Kolar'), ('Calicut', 'Calicut'), ('Nagapattanam', 'Nagapattanam'), ('Kottayam', 'Kottayam'), ('Howrah', 'Howrah'), ('Karur', 'Karur'), ('Rajamundry', 'Rajamundry'), ('Nadiad', 'Nadiad'), ('Ludhiana', 'Ludhiana'), ('Ujjire', 'Ujjire'), ('Margao', 'Margao'), ('Kumbakonam', 'Kumbakonam'), ('Mehsana', 'Mehsana'), ('Rajkot', 'Rajkot'), ('Ranipat', 'Ranipat'), ('Chittorgarh', 'Chittorgarh'), ('Varanasi', 'Varanasi'), ('Hubli', 'Hubli'), ('Kanpur', 'Kanpur'), ('Solapur', 'Solapur'), ('Ashok Nagar', 'Ashok Nagar'), ('Bhubaneswar', 'Bhubaneswar'), ('Westgodavari', 'Westgodavari'), ('Malegaon', 'Malegaon'), ('Kutch', 'Kutch'), ('Vaishali', 'Vaishali'), ('Trichy', 'Trichy'), ('Tiruppur', 'Tiruppur'), ('Gudivada', 'Gudivada'), ('Jammu', 'Jammu'), ('Nellore', 'Nellore'), ('Eluru', 'Eluru'), ('Kolkata', 'Kolkata'), ('Palakkad', 'Palakkad'), ('Anekal', 'Anekal'), ('Mangalore', 'Mangalore'), ('Sindhudurga', 'Sindhudurga'), ('Bharatpur', 'Bharatpur'), ('Bhosari', 'Bhosari'), ('Bhopal', 'Bhopal'), ('Moradabad', 'Moradabad'), ('Ranbennur', 'Ranbennur'), ('Sonitpur', 'Sonitpur'), ('Kanyakumari', 'Kanyakumari'), ('Baroda', 'Baroda'), ('Amravati', 'Amravati'), ('Raichur', 'Raichur'), ('Pondicherry', 'Pondicherry'), ('Mohali', 'Mohali'), ('Panchkula', 'Panchkula'), ('Aluva', 'Aluva'), ('Thiruvallur', 'Thiruvallur'), ('Pathanamthitta', 'Pathanamthitta'), ('Hapur', 'Hapur'), ('Ramanagaram', 'Ramanagaram'), ('Parbhani', 'Parbhani'), ('Manacaud', 'Manacaud'), ('Dhenkanal', 'Dhenkanal'), ('Tirunelveli', 'Tirunelveli'), ('Tiruchendur', 'Tiruchendur'), ('Delhi', 'Delhi'), ('Cochin', 'Cochin'), ('Tuticorin', 'Tuticorin'), ('Srinagar', 'Srinagar'), ('Krishna', 'Krishna'), ('Jabalpur', 'Jabalpur'), ('Rewari', 'Rewari'), ('Wardha', 'Wardha'), ('Mira Road', 'Mira Road'), ('Jind', 'Jind'), ('Nahan', 'Nahan'), ('Bangalore,', 'Bangalore,'), ('Ballabgarh', 'Ballabgarh'), ('Kothagudem', 'Kothagudem'), ('Pune', 'Pune'), ('Bellary', 'Bellary'), ('Vijayawada', 'Vijayawada'), ('Ananthapur', 'Ananthapur'), ('Tumkur', 'Tumkur'), ('Kanchipuram', 'Kanchipuram'), ('Udaipur', 'Udaipur'), ('Alwar', 'Alwar'), ('Bilaspur', 'Bilaspur'), ('Jalgaon', 'Jalgaon'), ('Tanjore', 'Tanjore'), ('Godhra', 'Godhra'), ('Nagarbhavi', 'Nagarbhavi'), ('Wayanad', 'Wayanad'), ('Kurukshetra', 'Kurukshetra'), ('Panjim', 'Panjim'), ('Bhavnagar', 'Bhavnagar'), ('Nainital', 'Nainital'), ('Shamshabad', 'Shamshabad'), ('Kengeri Upanagara', 'Kengeri Upanagara'), ('Barnala', 'Barnala'), ('Amraiwadi', 'Amraiwadi'), ('Shimoga', 'Shimoga'), ('Nagpur', 'Nagpur'), ('Patan', 'Patan'), ('Kollam', 'Kollam'), ('Hooghly', 'Hooghly'), ('Chikkaballapur', 'Chikkaballapur'), ('Bagalkot', 'Bagalkot'), ('Sonepat', 'Sonepat'), ('Gandhinagar', 'Gandhinagar'), ('Chanapatna', 'Chanapatna'), ('Cuddalore', 'Cuddalore'), ('Titagarh', 'Titagarh'), ('Faridabad', 'Faridabad'), ('Gangavathi', 'Gangavathi'), ('Nangloi', 'Nangloi'), ('Kozhicode', 'Kozhicode'), ('Tadepalligudam', 'Tadepalligudam'), ('Krishnagiri', 'Krishnagiri'), ('Karimnagar', 'Karimnagar'), ('Valapady', 'Valapady'), ('Kuzhithurai', 'Kuzhithurai'), ('Idukki', 'Idukki'), ('Vizag', 'Vizag'), ('Haldwani', 'Haldwani'), ('Erode', 'Erode'), ('Thane', 'Thane'), ('Dharmapuri', 'Dharmapuri'), ('Khurda', 'Khurda'), ('Miryalaguda', 'Miryalaguda'), ('Kunnamkulam', 'Kunnamkulam'), ('Belthangady', 'Belthangady'), ('Guntur', 'Guntur')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admission',
            name='state',
            field=models.CharField(blank=True, choices=[('Chattisgarh', 'Chattisgarh'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Bihar', 'Bihar'), ('Maharashtra', 'Maharashtra'), ('Assam', 'Assam'), ('Uttaranchal', 'Uttaranchal'), ('Delhi', 'Delhi'), ('Himachal Pradesh', 'Himachal Pradesh'), ('West Bengal', 'West Bengal'), ('Kerala', 'Kerala'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('Uttarakhand', 'Uttarakhand'), ('Tamilnadu', 'Tamilnadu'), ('Rajasthan', 'Rajasthan'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Jharkhand', 'Jharkhand'), ('Punjab', 'Punjab'), ('Karnataka', 'Karnataka'), ('Gujarat', 'Gujarat'), ('Goa', 'Goa'), ('Orissa', 'Orissa'), ('Haryana', 'Haryana')], default=None, max_length=100, null=True),
        ),
    ]