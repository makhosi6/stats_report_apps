<?php
$agent = [
    "payrollId" => 88,
    "firstName" => "Bob",
    "surname" => "Van",
    "idType" => "I",
    "idNumber" => "error",
    "email" => "bob@me...",
    "functionRole" => "01",
    "registrationNumber" => "Reg. No: 123456",
    "clientReference" => "Reference"
];
$validate_primitive_key_values = function ($key, $max_length = -1, $optional = false) use ($agent) {
    if (!isset($agent[$key])) {
        return $optional ? false : true;
    }

    /// check for empty values
    $value = is_numeric($agent[$key]) ? strval($agent[$key]) : trim($agent[$key]);
    if (!$optional && empty($value)) {
        return true;
    }

    /// check max len
    if ($max_length > 0 && strlen($value) > $max_length) {
        return true;
    }
    return false;
};
var_dump($validate_primitive_key_values('payrollId', 2));
var_dump($validate_primitive_key_values('firstName'));
var_dump($validate_primitive_key_values('surname'));
var_dump($validate_primitive_key_values('idNumber'));
var_dump($validate_primitive_key_values('idType', 1));
var_dump($validate_primitive_key_values('clientReference'));
var_dump($validate_primitive_key_values('email'));


