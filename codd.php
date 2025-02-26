<?php

function qlink_validate_agent(array $agent, string $action)
{
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

    // Validate payrollId
    if ($validate_primitive_key_values('payrollId') || !filter_var($agent['payrollId'], FILTER_VALIDATE_INT)) {
        throw new Exception("Invalid or missing 'payrollId'. It must be valid int/numeric value.");
    }

    // Validate idType
    $validIdTypes = ['I', 'F', 'P', 'T'];
    if ($validate_primitive_key_values('idType', 1) || !in_array($agent['idType'], $validIdTypes)) {
        throw new Exception("Invalid or missing 'idType'. It must be one of: " . implode(', ', $validIdTypes). ". One letter string");
    }

    // Validate idNumber
    if ($validate_primitive_key_values('idNumber')) {
        throw new Exception("Invalid or missing 'idNumber'. It must be a non-empty string");
    }

    if ($action === 'delete_agent') {
        // Validate reasonCode
        $changeReasonCodes = ['01', '02', '03', '04', '05', '06'];
        if ($validate_primitive_key_values('reasonCode', 2) || !in_array($agent['reasonCode'], $changeReasonCodes)) {
            throw new Exception("Invalid or missing 'reasonCode'. It must be one of: " . implode(', ', $changeReasonCodes) . "Two letter string");
        }
    } elseif (in_array($action, ['create_agent', 'update_agent'])) {
        // Validate firstName
        if ($validate_primitive_key_values('firstName', 30)) {
            throw new Exception("Invalid or missing 'firstName'. It must be a non-empty string of max 30 characters.");
        }

        // Validate surname
        if ($validate_primitive_key_values('surname', 30)) {
            throw new Exception("Invalid or missing 'surname'. It must be a non-empty string of max 30 characters.");
        }

        // Validate email
        if ($validate_primitive_key_values('email') || !filter_var($agent['email'], FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid or missing 'email'. It must be a valid email address.");
        }
        // Validate clientReference
        if ($validate_primitive_key_values('clientReference', 50, true)) {
            throw new Exception("Invalid or missing 'clientReference'. It must be a non-empty string of max 50 characters.");
        }

        if ($action === 'create_agent') {
            // Validate functionRole
            $validFunctionRoles = ['01', '02', '99'];
            if ($validate_primitive_key_values('functionRole', 2) || !in_array($agent['functionRole'], $validFunctionRoles)) {
                throw new Exception("Invalid or missing 'functionRole'. It must be one of: " . implode(', ', $validFunctionRoles));
            }

            // Validate registrationNumber
            if ($validate_primitive_key_values('registrationNumber', 50)) {
                throw new Exception("Invalid or missing 'registrationNumber'. It must be a non-empty string.");
            }
        }
    } else {
        throw new Exception("Invalid action!!! Supported actions are: create_agent, update_agent, delete_agent.");
    }

}
$x = filter_var('90', FILTER_VALIDATE_INT);
var_dump(!$x);

///
$delete_body = [
    "payrollId" => 88,
    "idType" => "I",
    "idNumber" => "99080...",
    "reasonCode" => "01",
];
qlink_validate_agent($delete_body, 'delete_agent');

///
$create_body = [
    "payrollId" => 88,
    "firstName" => "Bob",
    "surname" => "Van",
    "idType" => "I",
    "idNumber" => "99080...",
    "email" => "bob@domain.me",
    "functionRole" => "01",
    "registrationNumber" => "Reg. No: 123456",
    "clientReference" => "Reference"
];
qlink_validate_agent($create_body, 'create_agent');

////
$update_body = [
    "payrollId" => 88,
    "firstName" => "Rob",
    "surname" => "Van",
    "idType" => "I",
    "idNumber" => "99080...",
    "email" => "bob@domain.me",
    "clientReference" => "Reference"
];
qlink_validate_agent($update_body, 'update_agent');
