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

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5)`

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
As defined in Section 1.6.1.
### 1.3.3  Subscribers
As defined in Section 1.6.1.
### 1.3.4 Relying parties
“Relying Party” and “Application Software Supplier” are defined in Section 1.6.1. Current Members of the CA/Browser Forum who are Application Software Suppliers are listed here: https://cabforum.org/members.
### 1.3.5  Other participants
Other groups that have participated in the development of these Requirements include the AICPA/CICA WebTrust for Certification Authorities task force and the Accredited Conformity Assessment Bodies' Council (ACAB'c). Participation by such groups does not imply their endorsement, recommendation, or approval of the final product.
## 1.4  Certificate usage
The primary goal of these Requirements is to provide a framework where “reasonable assurance” may be provided to senders and recipients of email messages that the party identified in an S/MIME Certificate has control of the domain or email address being asserted. A variation of this use case is where an individual or organization digitally signs email to establish its authenticity and source of origin.  
### 1.4.1  Appropriate certificate uses

### 1.4.2 Prohibited certificate uses

## 1.5  Policy administration
This document may be revised from time to time, as appropriate, in accordance with procedures adopted by the CA/Browser Forum.  The CA/Browser Forum welcomes recommendations and suggestions regarding this standard by email at questions@cabforum.org. 
### 1.5.1  Organization administering the document
Contact information for the CA/Browser Forum is available here: https://cabforum.org/leadership/. In this section of a CA’s CPS, the CA shall provide a link to a web page or an email address for contacting the person or persons responsible for operation of the CA, including contact information for entities wishing to submit a Certificate Problem Report.
### 1.5.2  Contact person

### 1.5.3  Person determining CPS suitability for the policy

### 1.5.4  CPS approval procedures

## 1.6  Definitions and acronyms
###  1.6.1 Definitions

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

###  1.6.4 Conventions

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in these Requirements shall be interpreted in accordance with RFC 2119.

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES

## 2.1  Repositories

## 2.2  Publication of certification information

## 2.3  Time or frequency of publication

## 2.4  Access controls on repositories

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

The CA MUST verify that Applicant controls the email accounts associated with all email addresses referenced in the Certificate or has been authorized by the email account holder to act on the account holder’s behalf. 

<b>Note:</b> Email addresses may be listed in Subscriber Certificates using Rfc822Names in the subjectAltName extension or in Subordinate CA Certificates via Rfc822Names in
permittedSubtrees within the Name Constraints extension.

The CA's CP/CPS MUST specify the procedures that the CA employs to perform this verification. CAs SHALL maintain a record of which domain validation method, including relevant BR or SBR version number, used to validate every domain or email address in issued Certificates.
##### 3.2.2.2.1  Validating authority over email address via domain
Confirming the Applicant has been authorized by the email account holder to act on the account holder’s behalf by verifying the entity's control over the domain portion of the email address to be used in the Certificate.

The CA SHALL use only the approved methods in Section 3.2.2.4 of Version 1.7.3 of the BR to perform this verification

The CA SHALL NOT delegate validation of the domain portion of an email address.

Completed validations of Applicant authority may be valid for the issuance of multiple Certificates over time. In all cases, the validation must have been initiated within the time period specified in the relevant requirement (such as Section 4.2.1 of this document) prior to Certificate issuance. 

For purposes of domain validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.
##### 3.2.2.2.2  Validating control over email address via email
Confirming the Applicant's control over the email address by sending a Random Value via email and then receiving a confirming response utilizing the Random Value. The Random Value MUST be sent only to the address being validated and SHALL not be shared in any other way. 

The Random Value SHALL be unique in each email. 

The CA MAY resend the email in its entirety, including re-use of the Random Value, provided that the entire contents and recipient email address of the communication remain unchanged.

The Random Value SHALL remain valid for use in a confirming response for no more than 30 days from its creation. The CPS MAY specify a shorter validity period for Random Values, in which case the CA MUST follow its CPS.

Completed validations of Applicant control over the email address must be performed for each Certificate issuance.

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

### 4.9.2  Who can request revocation

### 4.9.3  Procedure for revocation request

### 4.9.4  Revocation request grace period

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

# 5. FACILITY, MANAGEMENT, AND OPERATIONAL CONTROLS (11)

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

# 6.  TECHNICAL SECURITY CONTROLS (11)

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

### 7.1.1  Version number(s)

### 7.1.2  Certificate extensions

### 7.1.3  Algorithm object identifiers

### 7.1.4  Name forms

### 7.1.5  Name constraints

### 7.1.6  Certificate policy object identifier

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

## 8.1  Frequency or circumstances of assessment

## 8.2  Identity/qualifications of assessor

## 8.3  Assessor's relationship to assessed entity

## 8.4  Topics covered by assessment

## 8.5  Actions taken as a result of deficiency

## 8.6  Communication of results

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

### 9.6.2  RA representations and warranties

### 9.6.3  Subscriber representations and warranties

### 9.6.4  Relying party representations and warranties

### 9.6.5  Representations and warranties of other participants

## 9.7  Disclaimers of warranties

## 9.8  Limitations of liability

## 9.9  Indemnities

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

### 9.16.4  Enforcement (attorneys' fees and waiver of rights)

### 9.16.5  Force Majeure

## 9.17  Other provisions