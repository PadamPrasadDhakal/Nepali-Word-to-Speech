from __future__ import print_function

nepali_number={
    'sunya':0,
    'ek':1,
    'dui':2,
    'teen':3,
    'tin':3,
    'chaar':4,
    'paach':5,
    'cha':6,
    'saat':7,
    'aath':8,
    'nau':9,
    'das':10,
    'egharah':11,
    'barah':12,
    'terah':13,
    'chaudah':14,
    'pandrah':15,
    'sorha':16,
    'satrah':17,
    'atharah':18,
    'unnaish':19,
    'biss':20,
    'ekkaish':21,
    'baaish':22,
    'teish':23,
    'chaubish':24,
    'pacchish':25,
    'chhabis':26,
    'sattaish':27,
    'atthaish':28,
    'untish':29,
    'tiss':30,
    'ektiss':31,
    'battiss':32,
    'teetiss':33,
    'chautiss':34,
    'paitiss':35,
    'chhattiss':36,
    'sattiss':37,
    'aathtiss':38,
    'unchalis':39,
    'chalis':40,
    'ekchalis':41,
    'bayachalis':42,
    'trichalis':43,
    'chauwaliss':44,
    'paitalish':45,
    'chayalish':46,
    'satchalis':47,
    'aathchalis':48,
    'unpachaas':49,
    'pachaas':50,
    'ekkaunna':51,
    'baunna':52,
    'tripanna':53,
    'chaunna':54,
    'pachpanna':55,
    'chapanna':56,
    'santauna':57,
    'anthaunna':58,
    'unhansatthi':59,
    'saxti':60,
    'eksaxti':61,
    'baisatthi':62,
    'trisatthi':63,
    'chausatthi':64,
    'paisatthi':65,
    'chaisatthi':66,
    'sadsatthi':67,
    'addsatthi':68,
    'unhansattari':69,
    'sattari':70,
    'ekhattar':71,
    'bahattar':72,
    'teerhattar':73,
    'chaurahattar':74,
    'pachattar':75,
    'chyahattar':76,
    'satahattar':77,
    'athattar':78,
    'unashi':79,
    'assi':80,
    'ekassi':81,
    'bayassi':82,
    'triyassi':83,
    'chaurassi':84,
    'paachasi':85,
    'chhayasi':86,
    'sataasi':87,
    'aathasi':88,
    'unhannabbe':89,
    'nabbae':90,
    'eknabbae':91,
    'bayanabbe':92,
    'teeranabbe':93,
    'chauranabbe':94,
    'panchanabbe':95,
    'chanayabbe':96,
    'santanabbe':97,
    'anthanabbe':98,
    'unhansaya':99,
    #others
    'saya':100,
    'hajar':1000,
    'lakh':100000,
    'karod':10000000,
    'arba':1000000000,
    'kharba':100000000000,
    'dasamalab':'.'
}


def get_numbers_info():
    print(nepali_number)

"""
function to form numeric multipliers for 10th-lakh, 10th-karod, 10th-thousand etc.

input: list of strings
return value: integer
"""

def number_formulation(num_words):
    nums=[]
    for n_word in num_words:
        nums.append(nepali_number[n_word])
    if len(nums)==13:
            return (nums[0]*nums[1] + nums[2]*nums[3] + nums[4]*nums[5] + nums[6]*nums[7] + nums[8]*nums[9] + nums[10]*nums[11] + nums[12])
    elif len(nums)==11:
            return (nums[0]*nums[1] + nums[2]*nums[3] + nums[4]*nums[5] + nums[6]*nums[7] + nums[8]*nums[9] + nums[10])
    elif len(nums)==9:
            return (nums[0]*nums[1] + nums[2]*nums[3] + nums[4]*nums[5] + nums[6]*nums[7] + nums[8])
    elif len(nums)==7:
            return (nums[0]*nums[1] + nums[2]*nums[3] + nums[4]*nums[5] + nums[6])
    elif len(nums)==5:
            return (nums[0]*nums[1] + nums[2]*nums[3] + nums[4])
    elif len(nums) == 4:
        return (nums[0] * nums[1]) + nums[2] + nums[3]
    elif len(nums) == 3:
        return nums[0] * nums[1] + nums[2]
    elif len(nums) == 2:
        if 1000 in nums:
            return nums[0] * nums[1]
        else:
            return nums[0] + nums[1]
    else:
        return nums[0]
    
"""
Convert decimal word to their numeric equivalent.
valid : only from 0(sunya) to 9(nau)

Arguments:
    decimal_words (list): List of words representing decimal digits

Returns:
    float: The decimal part as a float (e.g., ["two", "siz"] becomes 0.26)

Raises:
    ValueError: If any invalid decimal words are found
"""

def get_decimal(decimal_words):
  decimal_num_str = []
  invalid_dec = []

  for dec_w in decimal_words:
    if dec_w not in nepali_number:
      invalid_dec.append(dec_w)

  if invalid_dec:
    error_msg = f"Invalid decimal digits found: {', '.join(invalid_dec)}. Only words from 'zero' to 'nine' are allowed after 'point'."
    raise ValueError(error_msg)

  for dec_w in decimal_words:
    decimal_num_str.append(str(nepali_number[dec_w]))

  final_dec_str = '0.' + ''.join(decimal_num_str)
  return float(final_dec_str)

"""
Converts a textual number representation to its numerical value.

Features:
- Converts phrases like "ek lakh tin hajar cha saya nau" to 103609
- Supports decimal numbers with "dasamalab" (e.g., "dui dasamalab tin")
- Provides detailed error messages for invalid inputs

Arguments:
    number_sentence (str): A string containing the textual representation of a number

Returns:
    int or float: Numeric value based on there is presence of dasamalab or not(int or float resp)

Raises:
    ValueError: For invalid inputs, with specific error messages explaining the problem
"""
def word_to_num(number_sentence):
    if type(number_sentence) is not str:
        raise ValueError("Type of input is not string! Please enter a valid number word (e.g., 'tin hajar cha saya nau') for more info do get_numbers_info()")
        
    number_sentence = number_sentence.replace('-', ' ')
    number_sentence = number_sentence.lower() #converting input to lowercase
    
    if(number_sentence.isdigit()):  # return the number if user enters a number string
        return int(number_sentence)

