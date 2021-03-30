---
title: Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates
subtitle: Version X.Y.Z
author:
  - CA/Browser Forum
date: X Date, 2021
copyright: |
  Copyright 2021 CA/Browser Forum
  This work is licensed under the Creative Commons Attribution 4.0 International license.
---

# 1.  INTRODUCTION

## 1.1  Overview
This document describes an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements that are necessary for the issuance and management of Publicly-Trusted S/MIME Certificates

**Notice for Readers**

An S/MIME Certificate contains a public key bound to an email address, and may also contain the identity of a natural person or legal entity that controls such email address. The key pair can then be used to sign, verify, encrypt, and decrypt email. An S/MIME Certificate can be identified by the existence of an Extended Key Usage (EKU) Object Identifier (OID) of 1.3.6.1.5.5.7.3.4 for `emailProtection`.

The CP for the Issuance and Management of Publicly-Trusted S/MIME Certificates describes a subset of the requirements that a Certification Authority must meet in order to issue Publicly Trusted S/MIME Certificates. This document serves two purposes: to specify Baseline Requirements and to provide guidance and requirements for what a CA should include in its CPS. Except where explicitly stated otherwise, these Requirements apply only to relevant events that occur on or after DATE (the original effective date of these requirements).

These Requirements do not address all of the issues relevant to the issuance and management of Publicly-Trusted S/MIME Certificates. In accordance with RFC 3647 and to facilitate a comparison of other certificate policies and CPSs (e.g. for policy mapping), this document includes all sections of the RFC 3647 framework. However, rather than beginning with a “no stipulation” comment in all empty sections, the CA/Browser Forum initially leaves sections blank until a decision of “no stipulation” is made. The CA/Browser Forum may update these Requirements from time to time.

These Requirements do not address the issuance or management of Certificates by enterprises that operate their own Public Key Infrastructure for internal purposes only, and for which the Root Certificate is not distributed by any Application Software Supplier. These Requirements are applicable to all Certification Authorities within a chain of trust. They are to be flowed down from the Root Certification Authority through successive Subordinate Certification Authorities.

## 1.2  Document name and identification
This Certificate Policy (CP) contains the requirements for the issuance and management of Publicly-Trusted S/MIME Certificates, as adopted by the CA/Browser Forum.

The following Certificate Policy identifiers are reserved for use by CAs as a means of asserting compliance with this document (OID arc 2.23.140.1.5.x.y) as follows:

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5)}`

Where x may represent:

*  `mailbox-validation (1)`

*  `organization-validation (2)`

*  `sponsored-validation (3)`

*  `individual-validation (4)`

Where y may represent:

*  `strict (1)`

*  `multipurpose (2)`

*  `legacy (3)`

### 1.2.1  Revisions

|Version| Ballot|Description                       | Adopted  | Effective\*  |
|-------|-------|----------------------------------|----------| -----------|
|00     |       |Working draft                     |TBD       |TBD         |
\* Effective Date and Additionally Relevant Compliance Date(s)
  
## 1.3  PKI participants
The CA/Browser Forum is a voluntary organization of Certification Authorities and suppliers of Internet browser and other relying-party software applications including mail user agents (web-based or application based) and email service providers that process S/MIME Certificates.
### 1.3.1  Certification authorities
Certification Authority (CA) is defined in Section 1.6.1. Current CA Members of the CA/Browser Forum are listed here: https://cabforum.org/members.
### 1.3.2  Registration authorities
With the exception of sections __, the CA MAY delegate the performance of all, or any part, of Section 3.2 requirements to a Delegated Third Party, provided that the process as a whole fulfills all of the requirements of Section 3.2.

Before the CA authorizes a Delegated Third Party to perform a delegated function, the CA SHALL contractually require the Delegated Third Party to:

1. Meet the qualification requirements of Section 5.3.1, when applicable to the delegated function;
2. Retain documentation in accordance with Section 5.5.2;
3. Abide by the other provisions of these Requirements that are applicable to the delegated function; and
4. Comply with (a) the CA's Certificate Policy/Certification Practice Statement or (b) the Delegated Third Party's practice statement that the CA has verified complies with these Requirements.

The CA MAY designate an Enterprise RA to verify certificate requests from the Enterprise RA's own organization.  The CA SHALL NOT accept certificate requests authorized by an Enterprise RA unless the following requirements are satisfied:

1. The CA SHALL confirm that the requested Fully-Qualified Domain Name(s) are within the Enterprise RA's verified Domain Namespace.
2. If the certificate request includes a Subject name of a type other than a Fully-Qualified Domain Name, the CA SHALL confirm that the name is either that of the delegated enterprise, or an Affiliate of the delegated enterprise, or that the delegated enterprise is an agent of the named Subject. For example, the CA SHALL NOT issue a Certificate containing the Subject name "XYZ Co." on the authority of Enterprise RA "ABC Co.", unless the two companies are affiliated (see Section 3.2) or "ABC Co." is the agent of "XYZ Co". This requirement applies regardless of whether the accompanying requested Subject FQDN falls within the Domain Namespace of ABC Co.'s Registered Domain Name.

The CA SHALL impose these limitations as a contractual requirement on the Enterprise RA and monitor compliance by the Enterprise RA.
### 1.3.3  Subscribers
As defined in Section 1.6.1.
### 1.3.4 Relying parties
“Relying Party” and “Application Software Supplier” are defined in Section 1.6.1. Current Members of the CA/Browser Forum who are Application Software Suppliers are listed here: https://cabforum.org/members.
### 1.3.5  Other participants
Other groups that have participated in the development of these Requirements include the AICPA/CICA WebTrust for Certification Authorities task force and the Accredited Conformity Assessment Bodies' Council (ACAB'c). Participation by such groups does not imply their endorsement, recommendation, or approval of the final product.
## 1.4  Certificate usage
The primary goal of these Requirements is to provide a framework where “reasonable assurance” may be provided to senders and recipients of email messages that the party identified in an S/MIME Certificate has control of the domain or email address being asserted. A variation of this use case is where an individual or organization digitally signs email to establish its authenticity and source of origin.  
### 1.4.1  Appropriate certificate uses
The primary goal of these Requirements is to describe an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements for the issuance and management of Publicly-Trusted S/MIME Certificates. These Requirements also serve to inform users and help them to make informed decisions when relying on Certificates.
### 1.4.2 Prohibited certificate uses
No stipulation.
## 1.5  Policy administration
This document may be revised from time to time, as appropriate, in accordance with procedures adopted by the CA/Browser Forum.  The CA/Browser Forum welcomes recommendations and suggestions regarding this standard by email at questions@cabforum.org. 
### 1.5.1  Organization administering the document
No stipulation.
### 1.5.2  Contact person
Contact information for the CA/Browser Forum is available here: https://cabforum.org/leadership/. In this section of a CA’s CPS, the CA shall provide a link to a web page or an email address for contacting the person or persons responsible for operation of the CA, including contact information for entities wishing to submit a Certificate Problem Report.
### 1.5.3  Person determining CPS suitability for the policy
No stipulation.
### 1.5.4  CPS approval procedures
No stipulation.
## 1.6  Definitions and acronyms
###  1.6.1 Definitions
TBD
###  1.6.2 Acronyms

|Acronym   |Meaning                                                            |
|----------|-------------------------------------------------------------------|
|AICPA	   |American Institute of Certified Public Accountants |
|CA	       |Certification Authority |
|CAA	   |Certification Authority Authorization |
|CICA	   |Canadian Institute of Chartered Accountants |
|CP	       |Certificate Policy |
|CPS	   |Certification Practice Statement |
|CRL	   |Certificate Revocation List|
|DBA	   |Doing Business As |
|DNS	   |Domain Name System |
|FIPS	   |(US Government) Federal Information Processing Standard|
|IANA	   |Internet Assigned Numbers Authority |
|ICANN	   |Internet Corporation for Assigned Names and Numbers|
|ISO	   |International Organization for Standardization |
|NIST	   |(US Government) National Institute of Standards and Technology
|OCSP	   |Online Certificate Status Protocol|
|OID	   |Object Identifier|
|PKI	   |Public Key Infrastructure|
|RA	       |Registration Authority|
|S/MIME	   |Secure MIME (Multipurpose Internet Mail Extensions)|
|TLS	   |Transport Layer Security|
###  1.6.3 References
TBD
###  1.6.4 Conventions

The key words “SHALL”, “SHALL NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in these Requirements shall be interpreted in accordance with RFC 2119.

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES
The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement that describes in detail how the CA implements the latest version of these Requirements.
## 2.1  Repositories
The CA SHALL make revocation information for Subordinate CA Certificates and Subscriber Certificates available in accordance with this Policy.
## 2.2  Publication of certification information
The CA SHALL publicly disclose its Certificate Policy and/or Certification Practice Statement through an appropriate and readily accessible online means that is available on a 24x7 basis. The CA SHALL publicly disclose its CA business practices to the extent required by the CA's selected audit scheme (see Section 8.1).

The Certificate Policy and/or Certification Practice Statement SHALL be structured in accordance with RFC 3647 and SHALL include all material required by RFC 3647.

<u>EDITS REQUIRED:  Section 4.2 of a CA's Certificate Policy and/or Certification Practice Statement SHALL state the CA's policy or practice on processing CAA Records for Fully Qualified Domain Names; that policy shall be consistent with these Requirements. It shall clearly specify the set of Issuer Domain Names that the CA recognizes in CAA "issue" or "issuewild" records as permitting it to issue. The CA SHALL log all actions taken, if any, consistent with its processing practice.</u>

The CA SHALL publicly give effect to these Requirements and represent that it will adhere to the latest published version. The CA MAY fulfill this requirement by incorporating these Requirements directly into its Certificate Policy and/or Certification Practice Statements or by incorporating them by reference using a clause such as the following (which SHALL include a link to the official version of these Requirements):

> [Name of CA] conforms to the current version of the Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates published at http://www.cabforum.org. In the event of any inconsistency between this document and those Requirements, those Requirements take precedence over this document.

<u>EDITS REQUIRED: How about a requirement for TEST CERTS?</u>
## 2.3  Time or frequency of publication
The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement that describes in detail how the CA implements the latest version of these Requirements. The CA SHALL indicate conformance with this requirement by incrementing the version number and adding a dated changelog entry, even if no other changes are made to the document.
## 2.4  Access controls on repositories
The CA shall make its Repository publicly available in a read-only manner.
# 3. IDENTIFICATION AND AUTHENTICATION (11)

## 3.1  Naming

### 3.1.1  Types of names

### 3.1.2  Need for names to be meaningful

### 3.1.3  Anonymity or pseudonymity of subscribers

### 3.1.4  Rules for interpreting various name forms

### 3.1.5  Uniqueness of names

### 3.1.6  Recognition, authentication, and role of trademarks

## 3.2  Initial identity validation

### 3.2.1  Method to prove possession of private key

### 3.2.2  Authentication of organization and domain identity
#### 3.2.2.1  Authentication of organization identity
#### 3.2.2.2  Validation of domain authorization or control
This section defines the permitted processes and procedures for confirming the Applicant's control of the email addresses to be included in issued Certificates. 

The CA SHALL verify that Applicant controls the email accounts associated with all email addresses referenced in the Certificate or has been authorized by the email account holder to act on the account holder’s behalf. 

<b>Note:</b> Email addresses may be listed in Subscriber Certificates using Rfc822Names in the subjectAltName extension or in Subordinate CA Certificates via Rfc822Names in permittedSubtrees within the Name Constraints extension.

The CA's CP/CPS SHALL specify the procedures that the CA employs to perform this verification. CAs SHALL maintain a record of which domain validation method, including relevant BR or SBR version number, used to validate every domain or email address in issued Certificates.

Completed validations of Applicant authority may be valid for the issuance of multiple Certificates over time. In all cases, the validation SHALL have been initiated within the time period specified in the relevant requirement (such as Section 4.2.1 of this document) prior to Certificate issuance.
##### 3.2.2.2.1  Validating authority over email address via domain
Confirming the Applicant has been authorized by the email account holder to act on the account holder’s behalf by verifying the entity's control over the domain portion of the email address to be used in the Certificate.

The CA SHALL use only the approved methods in Section 3.2.2.4 of Version 1.7.3 of the Baseline Requirements to perform this verification

The CA SHALL NOT delegate validation of the domain portion of an email address. 

For purposes of domain validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.
##### 3.2.2.2.2  Validating control over email address via email
Confirming the Applicant's control over the email address by sending a Random Value via email and then receiving a confirming response utilizing the Random Value. The Random Value SHALL be sent only to the address being validated and SHALL not be shared in any other way. 

The Random Value SHALL be unique in each email. 

The CA MAY resend the email in its entirety, including re-use of the Random Value, provided that the entire contents and recipient email address of the communication remain unchanged.

The Random Value SHALL remain valid for use in a confirming response for no more than 30 days from its creation. The CPS MAY specify a shorter validity period for Random Values, in which case the CA SHALL follow its CPS.

#### 3.2.2.3  CAA Records
### 3.2.3  Authentication of individual identity

### 3.2.4  Non-verified subscriber information

### 3.2.5 Validation of authority

### 3.2.6  Criteria for interoperation

## 3.3  Identification and authentication for re-key requests

### 3.3.1  Identification and authentication for routine re-key

### 3.3.2  Identification and authentication for re-key after revocation

## 3.4 Identification and authentication for revocation request

# 4.  CERTIFICATE LIFE-CYCLE OPERATIONAL REQUIREMENTS

## 4.1  Certificate Application

### 4.1.1  Who can submit a certificate application

### 4.1.2  Enrollment process and responsibilities

## 4.2 Certificate application processing

### 4.2.1 Performing identification and authentication functions
Applicant information SHALL include, but not be limited to, at least one email address to be included in the Certificate's subjectAltName extension.

Section 6.3.2 limits the validity period of Subscriber Certificates. The CA MAY use the documents and data provided in Section 3.2 to verify certificate information, or may reuse previous validations themselves, provided that the CA obtained the data or document from a source specified under Section 3.2 or completed the validation itself no more than 398 days prior to issuing the Certificate.

In no case may a prior validation be reused if any data or document used in the prior validation was obtained more than the maximum time permitted for reuse of the data or document prior to issuing the Certificate.

After the change to any validation method specified in the Baseline Requirements or EV Guidelines, a CA may continue to reuse validation data or documents collected prior to the change, or the validation itself, for the period stated in this BR 4.2.1 unless otherwise specifically provided in a ballot.
### 4.2.2 Approval or rejection of certificate applications

### 4.2.3  Time to process certificate applications

## 4.3  Certificate issuance

### 4.3.1  CA actions during certificate issuance

### 4.3.2  Notification to subscriber by the CA of issuance of certificate

## 4.4  Certificate acceptance

### 4.4.1  Conduct constituting certificate acceptance

### 4.4.2  Publication of the certificate by the CA

### 4.4.3  Notification of certificate issuance by the CA to other entities

## 4.5 Key pair and certificate usage

### 4.5.1  Subscriber private key and certificate usage

### 4.5.2  Relying party public key and certificate usage

## 4.6  Certificate renewal

### 4.6.1  Circumstance for certificate renewal

### 4.6.2  Who may request renewal

### 4.6.3  Processing certificate renewal requests

### 4.6.4  Notification of new certificate issuance to subscriber

### 4.6.5  Conduct constituting acceptance of a renewal certificate

### 4.6.6  Publication of the renewal certificate by the CA

### 4.6.7  Notification of certificate issuance by the CA to other entities

## 4.7  Certificate re-key

### 4.7.1  Circumstance for certificate re-key

### 4.7.2  Who may request certification of a new public key

### 4.7.3  Processing certificate re-keying requests

### 4.7.4  Notification of new certificate issuance to subscriber

### 4.7.5  Conduct constituting acceptance of a re-keyed certificate

### 4.7.6  Publication of the re-keyed certificate by the CA

### 4.7.7  Notification of certificate issuance by the CA to other entities

## 4.8  Certificate modification

### 4.8.1  Circumstance for certificate modification

### 4.8.2  Who may request certificate modification

### 4.8.3  Processing certificate modification requests

### 4.8.4  Notification of new certificate issuance to subscriber

### 4.8.5  Conduct constituting acceptance of modified certificate

### 4.8.6  Publication of the modified certificate by the CA

### 4.8.7  Notification of certificate issuance by the CA to other entities

## 4.9  Certificate revocation and suspension

### 4.9.1  Circumstances for revocation
#### 4.9.1.1 Reasons for Revoking a Subscriber Certificate
The CA SHALL revoke a Certificate within 24 hours if one or more of the following occurs:
1. The Subscriber requests in writing that the CA revoke the Certificate;
2. The Subscriber notifies the CA that the original certificate request was not authorized and does not retroactively grant authorization;
3. The CA obtains evidence that the Subscriber's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise;
4. The CA is made aware of a demonstrated or proven method that can easily compute the Subscriber's Private Key based on the Public Key in the Certificate (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>);
5. The CA obtains evidence that the validation of domain authorization or control for any Fully-Qualified Domain Name or IP address in the Certificate should not be relied upon.
The CA SHOULD revoke a certificate within 24 hours and MUST revoke a Certificate within 5 days if one or more of the following occurs:
1. The Certificate no longer complies with the requirements of [Section 6.1.5](#615-key-sizes) and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
2. The CA obtains evidence that the Certificate was misused;
3. The CA is made aware that a Subscriber has violated one or more of its material obligations under the Subscriber Agreement or Terms of Use;
4. The CA is made aware of any circumstance indicating that use of a Fully-Qualified Domain Name or IP address in the Certificate is no longer legally permitted (e.g. a court or arbitrator has revoked a Domain Name Registrant's right to use the Domain Name, a relevant licensing or services agreement between the Domain Name Registrant and the Applicant has terminated, or the Domain Name Registrant has failed to renew the Domain Name);
5. The CA is made aware that a Wildcard Certificate has been used to authenticate a fraudulently misleading subordinate Fully-Qualified Domain Name;
6. The CA is made aware of a material change in the information contained in the Certificate;
7. The CA is made aware that the Certificate was not issued in accordance with these Requirements or the CA's Certificate Policy or Certification Practice Statement;
8. The CA determines or is made aware that any of the information appearing in the Certificate is inaccurate;
9. The CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the CA has made arrangements to continue maintaining the CRL/OCSP Repository;
10. Revocation is required by the CA's Certificate Policy and/or Certification Practice Statement; or
11. The CA is made aware of a demonstrated or proven method that exposes the Subscriber's Private Key to compromise or if there is clear evidence that the specific method used to generate the Private Key was flawed.
#### 4.9.1.2 Reasons for Revoking a Subordinate CA Certificate
The Issuing CA SHALL revoke a Subordinate CA Certificate within seven (7) days if one or more of the following occurs:
1. The Subordinate CA requests revocation in writing;
2. The Subordinate CA notifies the Issuing CA that the original certificate request was not authorized and does not retroactively grant authorization;
3. The Issuing CA obtains evidence that the Subordinate CA's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise or no longer complies with the requirements of [Section 6.1.5](#615-key-sizes) and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
4. The Issuing CA obtains evidence that the Certificate was misused;
5. The Issuing CA is made aware that the Certificate was not issued in accordance with or that Subordinate CA has not complied with this document or the applicable Certificate Policy or Certification Practice Statement;
6. The Issuing CA determines that any of the information appearing in the Certificate is inaccurate or misleading;
7. The Issuing CA or Subordinate CA ceases operations for any reason and has not made arrangements for another CA to provide revocation support for the Certificate;
8. The Issuing CA's or Subordinate CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the Issuing CA has made arrangements to continue maintaining the CRL/OCSP Repository; or
9. Revocation is required by the Issuing CA's Certificate Policy and/or Certification Practice Statement.
### 4.9.2  Who can request revocation
The Subscriber, RA, or Issuing CA can initiate revocation. Additionally, Subscribers, Relying Parties, Application Software Suppliers, and other third parties may submit Certificate Problem Reports informing the issuing CA of reasonable cause to revoke the certificate.
### 4.9.3  Procedure for revocation request
The CA SHALL provide a process for Subscribers to request revocation of their own Certificates. The process MUST be described in the CA's Certificate Policy or Certification Practice Statement. The CA SHALL maintain a continuous 24x7 ability to accept and respond to revocation requests and Certificate Problem Reports.

The CA SHALL provide Subscribers, Relying Parties, Application Software Suppliers, and other third parties with clear instructions for reporting suspected Private Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, inappropriate conduct, or any other matter related to Certificates. The CA SHALL publicly disclose the instructions through a readily accessible online means and in Section 1.5.2 of their CPS.
### 4.9.4  Revocation request grace period
No stipulation.

### 4.9.5  Time within which CA must process the revocation request

### 4.9.6  Revocation checking requirement for relying parties

### 4.9.7 CRL issuance frequency

### 4.9.8 Maximum latency for CRLs

### 4.9.9  On-line revocation/status checking availability

### 4.9.10 On-line revocation checking requirements

### 4.9.11 Other forms of revocation advertisements available

### 4.9.12 Special requirements re key compromise

### 4.9.13 Circumstances for suspension

### 4.9.14 Who can request suspension

### 4.9.15 Procedure for suspension request

### 4.9.16 Limits on suspension period

## 4.10  Certificate status services

### 4.10.1 Operational characteristics

### 4.10.2 Service availability

### 4.10.3 Optional features

## 4.11  End of subscription

## 4.12  Key escrow and recovery

### 4.12.1 Key escrow and recovery policy and practices

### 4.12.2 Session key encapsulation and recovery policy and practices

# 5. FACILITY, MANAGEMENT, AND OPERATIONAL CONTROLS

## 5.1  Physical controls

### 5.1.2  Physical access

### 5.1.3  Power and air conditioning

### 5.1.4  Water exposures

### 5.1.5  Fire prevention and protection

### 5.1.6  Media storage

### 5.1.7  Waste disposal

### 5.1.8  Off-site backup

## 5.2  Procedural controls

### 5.2.1  Trusted roles

### 5.2.2  Number of persons required per task

### 5.2.3  Identification and authentication for each role

### 5.2.4  Roles requiring separation of duties

## 5.3  Personnel controls

### 5.3.1  Qualifications, experience, and clearance requirements

### 5.3.2  Background check procedures

### 5.3.3  Training requirements

### 5.3.4  Retraining frequency and requirements

### 5.3.5  Job rotation frequency and sequence

### 5.3.6  Sanctions for unauthorized actions

### 5.3.7  Independent contractor requirements

### 5.3.8  Documentation supplied to personnel

## 5.4  Audit logging procedures

### 5.4.1  Types of events recorded

### 5.4.2  Frequency of processing log

### 5.4.3  Retention period for audit log

### 5.4.4  Protection of audit log

### 5.4.5  Audit log backup procedures

### 5.4.6  Audit collection system (internal vs. external)

### 5.4.7  Notification to event-causing subject

### 5.4.8  Vulnerability assessments

## 5.5  Records archival

### 5.5.1  Types of records archived

### 5.5.2  Retention period for archive

### 5.5.3  Protection of archive

### 5.5.4  Archive backup procedures

### 5.5.5  Requirements for time-stamping of records

### 5.5.6  Archive collection system (internal or external)

### 5.5.7  Procedures to obtain and verify archive information

## 5.6  Key changeover

## 5.7  Compromise and disaster recovery

### 5.7.1  Incident and compromise handling procedures

### 5.7.2  Computing resources, software, and/or data are corrupted

### 5.7.3  Entity private key compromise procedures

### 5.7.4  Business continuity capabilities after a disaster

## 5.8  CA or RA termination

# 6.  TECHNICAL SECURITY CONTROLS

## 6.1  Key pair generation and installation

### 6.1.1  Key pair generation

### 6.1.2  Private key delivery to subscriber

### 6.1.3  Public key delivery to certificate issuer

### 6.1.4  CA public key delivery to relying parties

### 6.1.5  Key sizes

### 6.1.6  Public key parameters generation and quality checking

### 6.1.7  Key usage purposes (as per X.509 v3 key usage field)

## 6.2  Private Key Protection and Cryptographic Module Engineering Controls

### 6.2.1  Cryptographic module standards and controls

### 6.2.2  Private key (n out of m) multi-person control

### 6.2.3  Private key escrow

### 6.2.4  Private key backup

### 6.2.5  Private key archival

### 6.2.6  Private key transfer into or from a cryptographic module

### 6.2.7  Private key storage on cryptographic module

### 6.2.8  Method of activating private key

### 6.2.9  Method of deactivating private key

### 6.2.10 Method of destroying private key

### 6.2.11 Cryptographic Module Rating

## 6.3  Other aspects of key pair management

### 6.3.1  Public key archival

### 6.3.2  Certificate operational periods and key pair usage periods

## 6.4  Activation data

### 6.4.1  Activation data generation and installation

### 6.4.2  Activation data protection

### 6.4.3  Other aspects of activation data

## 6.5  Computer security controls

### 6.5.1  Specific computer security technical requirements

### 6.5.2  Computer security rating

## 6.6  Life cycle technical controls

### 6.6.1  System development controls

### 6.6.2  Security management controls

### 6.6.3  Life cycle security controls

## 6.7  Network security controls

## 6.8  Time-stamping

# 7.  CERTIFICATE, CRL, AND OCSP PROFILES

## 7.1  Certificate profile

### 7.1.1  All certificates

All Certificates SHALL Have a Certificate structure with the following fields as follows:
​
|Name|ASN.1 Type and Constraints|Permitted Values|References|
|----|--------------------------|----------------|----------|
|tbsCertificate|`TBSCertificate`|See Section 7.1.1.1|[RFC 5280, Section 4.1.1.1](https://tools.ietf.org/html/rfc5280#section-4.1.1.1)|
|signatureAlgorithm|`AlgorithmIdentifier`|See Section 7.1.3.2 for permitted values. The value SHALL be equal to the `signature` field value of the TBSCertificate structure as defined in Section 7.1.1.1.|[RFC 5280, Section 4.1.1.2](https://tools.ietf.org/html/rfc5280#section-4.1.1.2)|
|signatureValue|`BIT STRING`|The digital signature computed upon the ASN.1 DER encoding of the `tbsCertificate` field|[RFC 5280, Section 4.1.1.3](https://tools.ietf.org/html/rfc5280#section-4.1.1.3)|

#### 7.1.1.1  TBSCertificate Structure    

All Certificates SHALL Have a TBSCertificate structure with the following fields:
​
|Name|ASN.1 Type and Constraints|Permitted Value(s)|References|
|----|--------------------------|------------------|----------|
|version|`INTEGER`|SHALL be v3(2)|[RFC 5280, Section 4.1.2.1](https://tools.ietf.org/html/rfc5280#section-4.1.2.1)|
|serialNumber|`INTEGER`<br>Encoded value SHALL be no longer than 20 octets|SHALL be a positive value that contains at least 64 bits of output from a CSPRNG|[RFC 5280, Section 4.1.2.2](https://tools.ietf.org/html/rfc5280#section-4.1.2.2)|
|signature|`AlgorithmIdentifier`|See Section 7.1.3.2 for permitted values. The value SHALL be equal to the `signatureAlgorithm` field value of the Certificate structure as defined in Section 7.1.1.|[RFC 5280, Section 4.1.2.3](https://tools.ietf.org/html/rfc5280#section-4.1.2.3)|
|issuer|`Name`|SHALL be byte-for-byte equal to the encoding of the `subject` field value of the issuing CA's Certificate|[RFC 5280, Section 4.1.2.4](https://tools.ietf.org/html/rfc5280#section-4.1.2.4)|
|validity|`Validity`|See Section 6.3.2.|[RFC 5280, Section 4.1.2.5](https://tools.ietf.org/html/rfc5280#section-4.1.2.5)|
|subject|`Name`|For Root and Subordinate CA Certificates, see Section 7.1.4.2.<br>For Subscriber Certificates, see Section 7.1.4.3.|[RFC 5280, Section 4.1.2.6](https://tools.ietf.org/html/rfc5280#section-4.1.2.6)|
|subjectPublicKeyInfo|`SubjectPublicKeyInfo`|See Sections 6.1.5, 6.1.6, and 7.1.3.1.|[RFC 5280, Section 4.1.2.7](https://tools.ietf.org/html/rfc5280#section-4.1.2.7)|
|issuerUniqueID|`BIT STRING`|SHALL NOT be present|[RFC 5280, Section 4.1.2.8](https://tools.ietf.org/html/rfc5280#section-4.1.2.8)|
|subjectUniqueID|`BIT STRING`|SHALL NOT be present|[RFC 5280, Section 4.1.2.8](https://tools.ietf.org/html/rfc5280#section-4.1.2.8)|
|extensions|`Extensions`|For Root Certificates, see Section 7.1.2.1.<br>For Subordinate CA Certificates, see Section 7.1.2.2.<br>For Subscriber Certificates, see Section 7.1.2.3.|[RFC 5280, Section 4.1.2.9](https://tools.ietf.org/html/rfc5280#section-4.1.2.9)|


### 7.1.2  Certificate extensions
#### 7.1.2.1  Root Certificates
To do

#### 7.1.2.2  Subordinate CA Certificates
To do

#### 7.1.2.3  Subscriber Certificates

The Section specifies the requirements for extensions included in Subscriber Certificates.

|Extension ID|Required?|Critical?|Permitted Value(s)|References|
|------------|---------|-----------|------------------|----------|
|authorityKeyIdentifier|Yes|No|The `keyIdentifer` field SHALL be present. `authorityCertIssuer` and `authorityCertSerialNumber` fields SHALL NOT be present.|[RFC 5280, Section 4.2.1.1](https://tools.ietf.org/html/rfc5280#section-4.2.1.1)|
|certificatePolicies|Yes|SHOULD NOT be critical|See Section 7.1.6.4 for the permitted `policyIdentifiers`.<br>For each included `policyIdentifer`, the CA MAY include `policyQualifiers`. If the `id-qt-cps` policyQualifier is included, then it SHALL contain a HTTP/HTTPS URL for the issuing CA's  Certification Practice Statement, Relying Party Agreement or other pointer to online information provided by the CA.|[RFC 5280, Section 4.2.1.4](https://tools.ietf.org/html/rfc5280#section-4.2.1.4)|
|subjectAlternateName|Yes|Yes if the `subject` is an empty sequence; otherwise, SHOULD NOT be critical|SHALL contain at least one `rfc822Name` value. SHALL NOT contain values of type: <ul><li> `dNSName`</li><li>`iPAddress`</li><li>`uniformResourceIdentifier`</li></ul>`otherName` values (such as Microsoft UPN) MAY be included if the value is identical to an `rfc822Name` expressed in the SAN extension.  Each `rfc822Name` and `otherName` value must be verified with publicly documented and audited measures in accordance with Section 3.2.2.|[RFC 5280, Section 4.2.1.6](https://tools.ietf.org/html/rfc5280#section-4.2.1.6)|
|extendedKeyUsage|Yes|No|`id-kp-emailProtection` SHALL be present.<br>`ip-kp-clientAuth` and/or `id-ms-kp-document-signing` MAY be present.<br>Other values SHOULD NOT be present.<br>`id-kp-serverauth` or `id-kp-codeSigning` or `id-kp-timeStamping` or `id-kp-ocspSigning` or `anyExtendedKeyUsage` SHALL NOT be present.|[RFC 5280, Section 4.2.1.12](https://tools.ietf.org/html/rfc5280#section-4.2.1.12)|
|authorityInfoAccess|Optional|No|SHOULD contain at least one `accessMethod` value of type `id-ad-ocsp` that specifies the HTTP URI of the issuing CA's OCSP responder. Additional `id-ad-ocsp` LDAP, FTP, or HTTP URIs MAY be specified.<br>SHOULD contain at least one `accessMethod` value of type `id-ad-caIssuers` that specifies the HTTP URI of the issuing CA's Certificate. Additional `id-ad-caIssuers` LDAP, FTP, or HTTP URIs MAY be specified.|[RFC 5280, Section 4.2.2.1](https://tools.ietf.org/html/rfc5280#section-4.2.2.1)|
|subjectKeyIdentifer|No, but SHOULD be included|No|A string that identifies the Public Key encoded in the Certificate's `subjectPublicKeyInfo`.|[RFC 5280, Section 4.2.1.2](https://tools.ietf.org/html/rfc5280#section-4.2.1.2)|
|keyUsage|Yes|Yes|If the `subjectPublicKeyInfo` encoded in the Certificate is of type `rsaEncryption`, then the following bits MAY be asserted:<ul><li>`digitalSignature`</li><li>`nonRepudiation`</li><li>`keyEncipherment`</li><li>`dataEncipherment`</li></ul>If the `subjectPublicKeyInfo` encoded in the Certificate is of type `id-ecPublicKey`, then the following bits MAY also be asserted:<ul><li>`digitalSignature`</li><li>`nonRepudiation`</li><li>`keyAgreement`</li><li>`encipherOnly` or `decipherOnly` only if `keyAgreement` is set</li></ul>Other bits SHALL NOT be asserted.|[RFC 5280, Section 4.2.1.3](https://tools.ietf.org/html/rfc5280#section-4.2.1.3)<br>[RFC 3279, Section 2.3.1](https://tools.ietf.org/html/rfc3279#section-2.3.1)<br>[RFC 5480, Section 3](https://tools.ietf.org/html/rfc5480#section-3) as updated by [RFC 8813, Section 3](https://tools.ietf.org/html/rfc8813#section-3)|
|basicConstraints|Optional|Either|The `cA` field SHALL NOT be set true. `pathLenConstraint` field SHALL NOT be present.|[RFC 5280, Section 4.2.1.9](https://tools.ietf.org/html/rfc5280#section-4.2.1.9)|
|crlDistributionPoints|Yes|No|SHALL contain at least one `distributionPoint` whose `fullName` value includes a GeneralName of type `URI` that includes a HTTP URI where the issuing CA's CRL can be retrieved.<br>Following additional publicly accessible `fullName` LDAP, FTP, or HTTP URIs MAY be specified.|[RFC 5280, Section 4.2.1.13](https://tools.ietf.org/html/rfc5280#section-4.2.1.13)|
|subjectDirectoryAttributes |No |No |May contain verified attributes which are not part of the Subject's Distinguished Name such as dateOfBirth, placeOfBirth, gender, countryOfCitizenship, or countryOfResidence.|[RFC 3739 Section 3.2.2](https://tools.ietf.org/html/rfc3739#section-3.2.2) |
|qcStatements|No |No |Indicates a Certificate that is issued as Qualified within a defined legal framework from an identified country or set of countries. |[RFC 3739 Section 3.2.6](https://tools.ietf.org/html/rfc3739#section-3.2.6) <br> ETSI EN 319 412-5, Section 4 |
|Legal Entity Identifier | No|No | A verified Legal Entity Identifier data record for LEI (1.3.6.1.4.1.52266.1) or for role (1.3.6.1.4.1.52266.2). | ISO 17442-1:2020, Clause 6 <br>ISO 17442-2:2020, Clause 4| 

#### 7.1.2.3.1  Key Usages
The keyUsage extension SHALL be present and SHALL contain one (and only one) type of the following key usage settings.  

|Type|`nonRepudiation`|`digitalSignature`|`keyEncipherment` <br /> or `keyAgreement`|
|:-:|:-:|:-:|:-:|
A | X |  |  |  
B | X |X |  |  
C |   |X |  |  
D |   |X |X |  
E |   |  |X |  
F | X |X |X |  

Type A, C, or E SHOULD be used to avoid mixed usage of keys.  

Certificates used to validate commitment to signed content SHALL be limited to type A, B, or F; of these alternatives type A SHOULD be used.

Certificates where the Private Key is escrowed by the Certificate Authority SHALL be limited to type D, E, or F; of these alternatives type E SHOULD be used.

### 7.1.3  Algorithm object identifiers

### 7.1.4  Name forms

### 7.1.5  Name constraints

### 7.1.6  Certificate policy object identifier
The following Certificate Policy identifiers are reserved for use by CAs as an optional means of asserting compliance with these Requirements as follows:


### 7.1.7  Usage of Policy Constraints extension

### 7.1.8  Policy qualifiers syntax and semantics

### 7.1.9 Processing semantics for the critical Certificate Policies extension

## 7.2  CRL profile

### 7.2.1  Version number(s)

### 7.2.2  CRL and CRL entry extensions

## 7.3  OCSP profile

### 7.3.1  Version number(s)

### 7.3.2  OCSP extensions

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS
The CA SHALL at all times:

1. Issue Certificates and operate its PKI in accordance with all law applicable to its business and the Certificates it issues in every jurisdiction in which it operates;
2. Comply with these Requirements;
3. Comply with the audit requirements set forth in this section; and
4. Be licensed as a CA in each jurisdiction where it operates, if licensing is required by the law of such jurisdiction for the issuance of Certificates.

**Implementers' Note**: The CA/Browser Forum continues to improve the S/MIME Baseline Requirements while WebTrust and ETSI also continue to update their audit criteria. We encourage all CAs to conform to each revision herein on the date specified without awaiting a corresponding update to an applicable audit criterion. In the event of a conflict between an existing audit criterion and a guideline revision, we will communicate with the audit community and attempt to resolve any uncertainty, and we will respond to implementation questions directed to <questions@cabforum.org>. 
## 8.1  Frequency or circumstances of assessment
Certificates that are capable of being used to issue new certificates MUST either be Technically Constrained in line with [Section 7.1.5](#715-name-constraints) and audited in line with [Section 8.7](#87-self-audits) only, or Unconstrained and fully audited in line with all remaining requirements from this section. A Certificate is deemed as capable of being used to issue new certificates if it contains an X.509v3 `basicConstraints` extension, with the `cA` boolean set to true and is therefore by definition a Root CA Certificate or a Subordinate CA Certificate.

The period during which the CA issues Certificates SHALL be divided into an unbroken sequence of audit periods. An audit period MUST NOT exceed one year in duration.

If the CA has a currently valid Audit Report indicating compliance with an audit scheme listed in [Section 8.4](#84-topics-covered-by-assessment), then no pre-issuance readiness assessment is necessary.

If the CA does not have a currently valid Audit Report indicating compliance with one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment), then, before issuing Publicly-Trusted Certificates, the CA SHALL successfully complete a point-in-time readiness assessment performed in accordance with applicable standards under one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment). The point-in-time readiness assessment SHALL be completed no earlier than twelve (12) months prior to issuing Publicly-Trusted Certificates and SHALL be followed by a complete audit under such scheme within ninety (90) days of issuing the first Publicly-Trusted Certificate.

## 8.2  Identity/qualifications of assessor
The CA's audit SHALL be performed by a Qualified Auditor. A Qualified Auditor means a natural person, Legal Entity, or group of natural persons or Legal Entities that collectively possess the following qualifications and skills:

1. Independence from the subject of the audit;
2. The ability to conduct an audit that addresses the criteria specified in an Eligible Audit Scheme (see [Section 8.4](#84-topics-covered-by-assessment));
3. Employs individuals who have proficiency in examining Public Key Infrastructure technology, information security tools and techniques, information technology and security auditing, and the third-party attestation function;
4. (For audits conducted in accordance with any one of the ETSI standards) accredited in accordance with ISO 17065 applying the requirements specified in ETSI EN 319 403;
5. (For audits conducted in accordance with the WebTrust standard) licensed by WebTrust;
6. Bound by law, government regulation, or professional code of ethics; and
7. Except in the case of an Internal Government Auditing Agency, maintains Professional Liability/Errors & Omissions insurance with policy limits of at least one million US dollars in coverage.
## 8.3  Assessor's relationship to assessed entity

## 8.4  Topics covered by assessment
The CA SHALL undergo an audit in accordance with one of the following schemes:

1. “WebTrust for CAs v2.1 or newer” AND “XXXX or newer”; or
2. ETSI EN 319 411-1 v1.2.2, which includes normative references to ETSI EN 319 401 (the latest version of the referenced ETSI documents should be applied); or
3. If a Government CA is required by its Certificate Policy to use a different internal audit scheme, it MAY use such scheme provided that the audit either
   a. encompasses all requirements of one of the above schemes or
   b. consists of comparable criteria that are available for public review.
Whichever scheme is chosen, it MUST incorporate periodic monitoring and/or accountability procedures to ensure that its audits continue to be conducted in accordance with the requirements of the scheme.

The audit MUST be conducted by a Qualified Auditor, as specified in [Section 8.2](#82-identityqualifications-of-assessor).

For Delegated Third Parties which are not Enterprise RAs, then the CA SHALL obtain an audit report, issued under the auditing standards that underlie the accepted audit schemes found in [Section 8.4](#84-topics-covered-by-assessment), that provides an opinion whether the Delegated Third Party's performance complies with either the Delegated Third Party's practice statement or the CA's Certificate Policy and/or Certification Practice Statement. If the opinion is that the Delegated Third Party does not comply, then the CA SHALL not allow the Delegated Third Party to continue performing delegated functions.

The audit period for the Delegated Third Party SHALL NOT exceed one year (ideally aligned with the CA's audit). However, if the CA or Delegated Third Party is under the operation, control, or supervision of a Government Entity and the audit scheme is completed over multiple years, then the annual audit MUST cover at least the core controls that are required to be audited annually by such scheme plus that portion of all non-core controls that are allowed to be conducted less frequently, but in no case may any non-core control be audited less often than once every three years.
## 8.5  Actions taken as a result of deficiency

## 8.6  Communication of results
The Audit Report SHALL state explicitly that it covers the relevant systems and processes used in the issuance of all Certificates that assert one or more of the policy identifiers listed in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers). The CA SHALL make the Audit Report publicly available.

The CA MUST make its Audit Report publicly available no later than three months after the end of the audit period. In the event of a delay greater than three months, the CA SHALL provide an explanatory letter signed by the Qualified Auditor.

The Audit Report MUST contain at least the following clearly-labelled information:

1. Name of the organization being audited;
2. Name and address of the organization performing the audit;
3. The SHA-256 fingerprint of all Roots and Subordinate CA Certificates, including Cross Certificates, that were in-scope of the audit;
4. Audit criteria, with version number(s), that were used to audit each of the certificates (and associated keys);
5. A list of the CA policy documents, with version numbers, referenced during the audit;
6. Whether the audit assessed a period of time or a point in time;
7. The start date and end date of the Audit Period, for those that cover a period of time;
8. The point in time date, for those that are for a point in time;
9. The date the report was issued, which will necessarily be after the end date or point in time date; 
10. (For audits conducted in accordance with any of the ETSI standards) a statement to indicate if the audit was a full audit or a surveillance audit, and which portions of the criteria were applied and evaluated, e.g. DVCP, OVCP, NCP, NCP+, LCP, EVCP, EVCP+, QCP-w, Part 1 (General Requirements), and/or Part 2 (Requirements for Trust Service Providers); and
11. (For audits conducted in accordance with any of the ETSI standards) a statement to indicate that the auditor referenced the applicable CA/Browser Forum criteria, such as this document, and the version used.

An authoritative English language version of the publicly available audit information MUST be provided by the Qualified Auditor and the CA SHALL ensure it is publicly available.

The Audit Report MUST be available as a PDF, and SHALL be text searchable for all information required. Each SHA-256 fingerprint within the Audit Report MUST be uppercase letters and MUST NOT contain colons, spaces, or line feeds.

## 8.7 Review of Enterprise RA or Technically Constrained Subordinate CA

The CA SHALL review the practices and procedures of each Enterprise RA or Technically Constrained Subordinate CA to ensure that each such entity is in compliance with these Requirements and the relevant Certificate Policy and/or Certification Practice Statement.

The CA SHALL internally audit the compliance of each Enterprise RA or Technically Constrained Subordinate CA with these Requirements on an annual basis.

# 9. OTHER BUSINESS AND LEGAL MATTERS

## 9.1  Fees

### 9.1.1  Certificate issuance or renewal fees

### 9.1.2  Certificate access fees

### 9.1.3  Revocation or status information access fees

### 9.1.4  Fees for other services

### 9.1.5  Refund policy

## 9.2  Financial responsibility

### 9.2.1  Insurance coverage

### 9.2.2  Other assets

### 9.2.3  Insurance or warranty coverage for end-entities

## 9.3  Confidentiality of business information

### 9.3.1  Scope of confidential information

### 9.3.2  Information not within the scope of confidential information

### 9.3.3  Responsibility to protect confidential information

## 9.4  Privacy of personal information

### 9.4.1  Privacy plan

### 9.4.2  Information treated as private

### 9.4.3  Information not deemed private

### 9.4.4  Responsibility to protect private information

### 9.4.5  Notice and consent to use private information

### 9.4.6 Disclosure pursuant to judicial or administrative process

### 9.4.7  Other information disclosure circumstances

## 9.5  Intellectual property rights

## 9.6  Representations and warranties

### 9.6.1  CA representations and warranties
For any Certificate in a hierarchy capable of being used for S/MIME, CAs SHALL revoke Certificates upon the occurrence of any of the following events:
1.  the Subscriber indicates that the original Certificate request was not authorized and does not retroactively grant authorization;
2.  the CA obtains reasonable evidence that the Subscriber’s Private Key (corresponding to the Public Key in the Certificate) has been compromised or is suspected of compromise;
3. the CA obtains reasonable evidence that the Certificate has been used for a purpose outside of that indicated in the Certificate or in the CA's Subscriber agreement;
4. the CA receives notice or otherwise becomes aware that a Subscriber has violated one or more of its material obligations under the Subscriber agreement;
5. the CA receives notice or otherwise becomes aware of any circumstance indicating that use of the email address in the Certificate is no longer legally permitted;
6. the CA receives notice or otherwise becomes aware of a material change in the information contained in the Certificate;
7. a determination that the Certificate was not issued in accordance with the CA’s Certificate Policy or Certification Practice Statement;
8. the CA determines that any of the information appearing in the Certificate is not accurate;
9. the CA ceases operations for any reason and has not arranged for another CA to provide revocation support for the Certificate;
10. the CA Private Key used in issuing the Certificate is suspected to have been compromised;
11. such additional revocation events as the CA publishes in its policy documentation; or
12. the Certificate was issued in violation of the then-current version of these requirements.
### 9.6.2  RA representations and warranties

### 9.6.3  Subscriber representations and warranties

### 9.6.4  Relying party representations and warranties

### 9.6.5  Representations and warranties of other participants

## 9.7  Disclaimers of warranties

## 9.8  Limitations of liability
For delegated tasks, the CA and any Delegated Third Party MAY allocate liability between themselves contractually as they determine, but the CA SHALL remain fully responsible for the performance of all parties in accordance with these Requirements, as if the tasks had not been delegated.

If the CA has issued and managed the Certificate in compliance with these Requirements and its Certificate Policy and/or Certification Practice Statement, the CA MAY disclaim liability to the Certificate Beneficiaries or any other third parties for any losses suffered as a result of use or reliance on such Certificate beyond those specified in the CA's Certificate Policy and/or Certification Practice Statement. If the CA has not issued or managed the Certificate in compliance with these Requirements and its Certificate Policy and/or Certification Practice Statement, the CA MAY seek to limit its liability to the Subscriber and to Relying Parties, regardless of the cause of action or legal theory involved, for any and all claims, losses or damages suffered as a result of the use or reliance on such Certificate by any appropriate means that the CA desires. If the CA chooses to limit its liability for Certificates that are not issued or managed in compliance with these Requirements or its Certificate Policy and/or Certification Practice Statement, then the CA SHALL include the limitations on liability in the CA's Certificate Policy and/or Certification Practice Statement.
## 9.9  Indemnities
Notwithstanding any limitations on its liability to Subscribers and Relying Parties, the CA understands and acknowledges that the Application Software Suppliers who have a Root Certificate distribution agreement in place with the Root CA do not assume any obligation or potential liability of the CA under these Requirements or that otherwise might exist because of the issuance or maintenance of Certificates or reliance thereon by Relying Parties or others. Thus, except in the case where the CA is a government entity, the CA SHALL defend, indemnify, and hold harmless each Application Software Supplier for any and all claims, damages, and losses suffered by such Application Software Supplier related to a Certificate issued by the CA, regardless of the cause of action or legal theory involved. This does not apply, however, to any claim, damages, or loss suffered by such Application Software Supplier related to a Certificate issued by the CA where such claim, damage, or loss was directly caused by such Application Software Supplier's software displaying as not trustworthy a Certificate that is still valid, or displaying as trustworthy: (1) a Certificate that has expired, or (2) a Certificate that has been revoked (but only in cases where the revocation status is currently available from the CA online, and the application software either failed to check such status or ignored an indication of revoked status).
## 9.10  Term and termination

### 9.10.1  Term

### 9.10.2  Termination

### 9.10.3  Effect of termination and survival

## 9.11  Individual notices and communications with participants

## 9.12  Amendments

### 9.12.1  Procedure for amendment

### 9.12.2  Notification mechanism and period

### 9.12.3  Circumstances under which OID must be changed

## 9.13  Dispute resolution provisions

## 9.14  Governing law

## 9.15  Compliance with applicable law

## 9.16  Miscellaneous provisions

### 9.16.1  Entire agreement

### 9.16.2  Assignment

### 9.16.3  Severability
In the event of a conflict between these Requirements and a law, regulation or government order (hereinafter ‘Law’) of any jurisdiction in which a CA operates or issues certificates, a CA MAY modify any conflicting requirement to the minimum extent necessary to make the requirement valid and legal in the jurisdiction. This applies only to operations or certificate issuances that are subject to that Law. In such event, the CA SHALL immediately (and prior to issuing a certificate under the modified requirement) include in Section 9.16.3 of the CA’s CPS a detailed reference to the Law requiring a modification of these Requirements under this section, and the specific modification to these Requirements implemented by the CA.

The CA SHALL also (prior to issuing a certificate under the modified requirement) notify the CA/Browser Forum of the relevant information newly added to its CPS by sending a message to questions@cabforum.org and receiving confirmation that it has been posted to the Public Mailing List and is indexed in the Public Mail Archives available at https://cabforum.org/pipermail/public/ (or such other email addresses and links as the Forum may designate), so that the CA/Browser Forum may consider possible revisions to these Requirements accordingly.

Any modification to CA practice enabled under this section SHALL be discontinued if and when the Law no longer applies, or these Requirements are modified to make it possible to comply with both them and the Law simultaneously. An appropriate change in practice, modification to the CA’s CPS and a notice to the CA/Browser Forum, as outlined above, SHALL be made within 90 days.

### 9.16.4  Enforcement (attorneys' fees and waiver of rights)

### 9.16.5  Force Majeure

## 9.17  Other provisions