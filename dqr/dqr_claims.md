Data Quality Report for: Provider-Facility Affiliated Claims

Total number of rows: 108280

Missing Values Information:
 Empty DataFrame
Columns: [Missing Values, Percentage (%)]
Index: [] 

Number of duplicate rows: 0

Data Types:
 Clinician NPI                    int64
Facility NPI                     int64
Healthcare Organization Name    object
class                           object
year                             int64
quarter                          int64
total_claims                     int64
total_patients                   int64
dtype: object 

Statistics for Numeric Columns:
        Clinician NPI  Facility NPI           year        quarter  \
count   1.082800e+05  1.082800e+05  108280.000000  108280.000000   
mean    1.502130e+09  1.448820e+09    2021.521407       2.534226   
std     2.873316e+08  2.824658e+08       0.499544       1.121829   
min     1.003000e+09  1.003855e+09    2021.000000       1.000000   
25%     1.255592e+09  1.194763e+09    2021.000000       2.000000   
50%     1.508279e+09  1.679526e+09    2022.000000       3.000000   
75%     1.750321e+09  1.679526e+09    2022.000000       4.000000   
max     1.992995e+09  1.710952e+09    2022.000000       4.000000   

        total_claims  total_patients  
count  108280.000000   108280.000000  
mean      146.649723      122.044671  
std       532.428871      407.556409  
min         0.000000        0.000000  
25%         0.000000        0.000000  
50%        19.000000       16.000000  
75%       151.000000      119.000000  
max     58044.000000    41511.000000   

-------------------------------------------
