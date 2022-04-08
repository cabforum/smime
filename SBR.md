---
title: Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates
subtitle: Version X.Y.Z
author:
  - CA/Browser Forum
date: X Date, 2022
copyright: |
  Copyright 2022 CA/Browser Forum
  This work is licensed under the Creative Commons Attribution 4.0 International license.
---

# 1. INTRODUCTION
**This is a pre-release draft of the S/MIME Baseline Requirements (SBR). This draft has not yet been balloted to become a CA/Browser Forum standard. Comments are welcomed.**

## 1.1 Overview

This S/MIME Baseline Requirements document describes an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements that are necessary for the issuance and management of Publicly-Trusted S/MIME Certificates.

An S/MIME Certificate for the purposes of this document can be identified by the existence of an Extended Key Usage (EKU) for `emailProtection` (OID: 1.3.6.1.5.5.7.3.4) and the inclusion of a `rfc822Name` or an `otherName` of type `id-on-SmtpUTF8Mailbox` in the `subjectAltName` extension.

**Notice for Readers**

An S/MIME Certificate contains a public key bound to an email address and MAY also contain the identity of a natural person or legal entity that controls such email address. The key pair can then be used to sign, verify, encrypt, and decrypt email. 

This Certificate Policy (CP) describes a subset of the requirements that a CA MUST meet in order to issue Publicly-Trusted S/MIME Certificates. This document serves two purposes: to specify Baseline Requirements and to provide guidance and requirements for what a CA should include in its Certification Practice Statement (CPS). These Requirements apply only to relevant events that occur on or after DATE (the original effective date of these Requirements).

These Requirements do not address all of the issues relevant to the issuance and management of Publicly-Trusted S/MIME Certificates. To facilitate a comparison of other CP and/or CPS (e.g., for policy mapping), this document includes all sections of the [RFC 3647](https://datatracker.ietf.org/doc/html/rfc3647) framework. The CA/Browser Forum MAY update these Requirements from time to time.

These Requirements do not address the issuance or management of Certificates by enterprises that operate their own Public Key Infrastructure for internal purposes only, and for which the Root CA Certificate is not distributed by any Application Software Supplier. These Requirements are applicable to all Certification Authorities within a chain of trust. They are to be flowed down from the Root CA through successive Subordinate CAs.

## 1.2 Document name and identification

This Certificate Policy contains the Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates, as adopted by the CA/Browser Forum.

The following Certificate Policy identifiers are reserved for use by CAs as a means of asserting compliance with this document (OID arc 2.23.140.1.5) as follows:

**Mailbox-validated**  
`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) mailbox-validated (1) legacy (1)}` (2.23.140.1.5.1.1); and  

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) mailbox-validated (1) multipurpose (2)}` (2.23.140.1.5.1.2); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) mailbox-validated (1) strict (3)}` (2.23.140.1.5.1.3); and 

**Organization-validated**  
`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) organization-validated (2) legacy (1)}` (2.23.140.1.5.2.1); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) organization-validated (2) multipurpose (2)}` (2.23.140.1.5.2.2); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) organization-validated (2) strict (3)}` (2.23.140.1.5.2.3); and 

**Sponsor-validated**  
`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) sponsor-validated (3) legacy (1)}` (2.23.140.1.5.3.1); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) sponsor-validated (3) multipurpose (2)}` (2.23.140.1.5.3.2); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) sponsor-validated (3) strict (3)}` (2.23.140.1.5.3.3); and 

**Individual-validated**  
`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) individual-validated (4) legacy (1)}` (2.23.140.1.5.4.1); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) individual-validated (4) multipurpose (2)}` (2.23.140.1.5.4.2); and 

`{joint-iso-itu-t(2) international-organizations(23) ca-browser-forum(140) certificate-policies(1) smime-baseline(5) individual-validated (4) strict (3)}` (2.23.140.1.5.4.3). 

### 1.2.1 Revisions

|Version| Ballot|Description                       | Adopted  | Effective\*  |
|------|-------|----------------------------------|----------| -----------|
| 00   | 00    |Version 1.0 of the S/MIME Baseline Requirements adopted | Adoption date | Adoption date plus 10 months |

\* Effective Date and Additionally Relevant Compliance Date(s)
  
## 1.3 PKI participants

The CA/Browser Forum is a voluntary organization of Certification Authorities and Application Software Suppliers including providers of Internet browser and other relying-party software applications, such as mail user agents (web-based or application based) and email service providers that process S/MIME Certificates.

### 1.3.1 Certification authorities

Certification Authority (CA) is defined in [Section 1.6.1](#161-definitions). Current CA Members of the CA/Browser Forum are listed at https://cabforum.org/members.

### 1.3.2 Registration authorities

With the exception of [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control), the CA MAY delegate the performance of all, or any part, of [Section 3.2](#32-initial-identity-validation) requirements to a Delegated Third Party, provided that the process as a whole fulfills all of the requirements of [Section 3.2](#32-initial-identity-validation).

Before the CA authorizes a Delegated Third Party to perform a delegated function, the CA SHALL contractually require the Delegated Third Party to:

1. Meet the qualification requirements of [Section 5.3.1](#531-qualifications-experience-and-clearance-requirements), when applicable to the delegated function;
2. Retain documentation in accordance with [Section 5.5.2](#552-retention-period-for-archive);
3. Abide by the other provisions of these Requirements that are applicable to the delegated function; and
4. Comply with (a) the CA's CP and/or CPS or (b) the Delegated Third Party's practice statement that the CA has verified complies with these Requirements.

#### 1.3.2.1 Enterprise registration authorities

The CA MAY designate an Enterprise Registration Authority (RA) to verify Certificate Requests from the Enterprise RA's own organization. The CA SHALL NOT accept Certificate Requests authorized by an Enterprise RA unless the following requirements are satisfied:

1. If the Certificate Request is for an `Organization-validated` or `Sponsor-validated` profile, the CA SHALL confirm that the Enterprise RA has authorization or control of the requested email domains in accordance with [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain) or [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers). The CA SHALL confirm that the `subject:organizationName` name is either that of the delegated enterprise, or an Affiliate of the delegated enterprise, or that the delegated enterprise is an agent of the named Subject. For example, the CA SHALL NOT issue a Certificate containing the Subject name "XYZ Co." on the authority of Enterprise RA "ABC Co.", unless the two companies are Affiliated as defined in [Section 3.2](#32-initial-identity-validation) or "ABC Co." is the agent of "XYZ Co". This requirement applies regardless of whether the accompanying requested email domain falls within the subdomains of ABC Co.'s Registered Domain Name.

2. If the Certificate Request is for a `Mailbox-validated` profile, the CA SHALL confirm that the mailbox holder has control of the requested email domains in accordance with [Section 3.2.2.2](#3222-validating-control-over-mailbox-via-email).

The CA SHALL impose these limitations as a contractual requirement on the Enterprise RA and monitor compliance by the Enterprise RA in accordance with [Section 8.8](#88-review-of-enterprise-ra-or-technically-constrained-subordinate-ca).

### 1.3.3 Subscribers

As defined in [Section 1.6.1](#16-definitions-and-acronyms).

### 1.3.4 Relying parties

“Relying Party” and “Application Software Supplier” are defined in [Section 1.6.1](#16-definitions-and-acronyms). Current Members of the CA/Browser Forum who are Application Software Suppliers are listed at https://cabforum.org/members.

### 1.3.5 Other participants

Other groups that have participated in the development of these Requirements include the CPA Canada WebTrust for Certification Authorities task force and the Accredited Conformity Assessment Bodies’ Council (ACAB’C). Participation by these groups does not imply their endorsement, recommendation, or approval of the final product.

## 1.4 Certificate usage

The primary goal of these Requirements is to provide a framework of “reasonable assurance” to senders and recipients of email messages that the party identified in an S/MIME Certificate has control of the domain or email address being asserted. A variation of this use case is where an individual or organization digitally signs email to establish its authenticity and source of origin. 

### 1.4.1 Appropriate certificate uses

The primary goal of these Requirements is to describe an integrated set of technologies, protocols, identity-proofing, lifecycle management, and auditing requirements for the issuance and management of Publicly-Trusted S/MIME Certificates. These Requirements also serve to inform users and help them to make informed decisions when relying on Certificates.

### 1.4.2 Prohibited certificate uses

No stipulation.

## 1.5 Policy administration

This document MAY be revised from time to time, as appropriate, in accordance with procedures adopted by the CA/Browser Forum. The CA/Browser Forum welcomes recommendations and suggestions regarding this standard by email at <questions@cabforum.org>. 

### 1.5.1 Organization administering the document

No stipulation.

### 1.5.2 Contact person

Contact information for the CA/Browser Forum is available at https://cabforum.org/leadership/. In this section of a CA’s CPS, the CA SHALL provide a link to a web page or an email address for contacting the person or persons responsible for operation of the CA, including contact information for entities wishing to submit a Certificate Problem Report or revocation request.

### 1.5.3 Person determining CPS suitability for the policy

No stipulation.

### 1.5.4 CPS approval procedures

No stipulation.

## 1.6 Definitions and acronyms

The Definitions found in the CA/Browser Forum's Network and Certificate System Security Requirements are incorporated by reference as if fully set forth herein.

### 1.6.1 Definitions

**Accounting Practitioner**: A certified public accountant, chartered accountant, or a person with an equivalent license within the country of the Applicant's Jurisdiction of Incorporation or Registration or any jurisdiction where the Applicant maintains an office or physical facility; provided that an accounting standards body in the jurisdiction maintains full (not "suspended" or "associate") membership status with the International Federation of Accountants.

**Affiliate**: A corporation, partnership, joint venture or other entity controlling, controlled by, or under common control with another entity, or an agency, department, political subdivision, or any entity operating under the direct control of a Government Entity.

**Applicant**: The natural person or Legal Entity that applies for (or seeks renewal of) a Certificate. Once the Certificate issues, the Applicant is referred to as the Subscriber. For Certificates issued to devices, the Applicant is the entity that controls or operates the device named in the Certificate, even if the device is sending the actual Certificate Request.

**Applicant Representative**: A natural person or human sponsor who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant:

  i. who signs and submits, or approves a Certificate Request on behalf of the Applicant, and/or
  ii. who signs and submits a Subscriber Agreement on behalf of the Applicant, and/or
  iii. who acknowledges the Terms of Use on behalf of the Applicant when the Applicant is an Affiliate of the CA or is the CA.

**Application Software Supplier**: A supplier of email client software or other relying-party application software such as mail user agents (web-based or application based) and email service providers that process S/MIME Certificates.

**Attestation Letter**: A letter attesting that Subject Information is correct written by an accountant, lawyer, government official, or other reliable third party customarily relied upon for such information.

**Audit Period**: In a period-of-time audit, the period between the first day (start) and the last day of operations (end) covered by the auditors in their engagement. (This is not the same as the period of time when the auditors are on-site at the CA.) The coverage rules and maximum length of audit periods are defined in [Section 8.1](#81--frequency-or-circumstances-of-assessment).

**Audit Report**: A report from a Qualified Auditor stating the Qualified Auditor's opinion on whether an entity's processes and controls comply with the mandatory provisions of these Requirements.

**Business Entity**: Any entity that is not a Private Organization, Government Entity, or Non-Commercial Entity as defined herein. Examples include, but are not limited to, general partnerships, unincorporated associations, sole proprietorships, etc.

**CAA**: From [RFC 8659](http://tools.ietf.org/html/rfc8659): "The Certification Authority Authorization (CAA) DNS Resource Record allows a DNS domain name holder to specify one or more Certification Authorities (CAs) authorized to issue Certificates for that domain name. CAA Resource Records allow a public CA to implement additional controls to reduce the risk of unintended Certificate mis-issue."

**CA Key Pair**: A Key Pair where the Public Key appears as the Subject Public Key Info in one or more Root CA Certificate(s) and/or Subordinate CA Certificate(s).

**Certificate**: An electronic document that uses a digital signature to bind a public key and an identity.

**Certificate Approver**: A natural person who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant to

  i. act as a Certificate Requester and to authorize other employees or third parties to act as a Certificate Requester, and
  ii. to approve Certificate Requests submitted by other Certificate Requesters.

**Certificate Data**: Certificate requests and data related thereto (whether obtained from the Applicant or otherwise) in the CA's possession or control or to which the CA has access.

**Certificate Management Process**: Processes, practices, and procedures associated with the use of keys, software, and hardware, by which the CA verifies Certificate Data, issues Certificates, maintains a Repository, and revokes Certificates.

**Certificate Policy (or CP)**: A set of rules that indicates the applicability of a named Certificate to a particular community and/or PKI implementation with common security requirements.

**Certificate Problem Report**: Complaint of suspected Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, or inappropriate conduct related to Certificates.

**Certificate Revocation List**: A regularly updated time-stamped list of revoked Certificates that is created and digitally signed by the CA that issued the Certificates.

**Certification Authority (or CA)**: An organization that is responsible for the creation, issuance, revocation, and management of Certificates. The term applies equally to both Root CAs and Subordinate CAs.

**Certification Practice Statement (or CPS)**: One of several documents forming the governance framework in which Certificates are created, issued, managed, and used.

**Certificate Profile**: A set of documents or files that defines requirements for Certificate content and Certificate extensions in accordance with [Section 7](#7-certificate-crl-and-ocsp-profiles). e.g. a Section in a CA’s CPS or a Certificate template file used by CA software.

**Certificate Requester**: A natural person who is either the Applicant, employed by the Applicant, an authorized agent who has express authority to represent the Applicant, or a third party that completes and submits a Certificate Request on behalf of the Applicant.

**Contract Signer**: A natural person who is either the Applicant, employed by the Applicant, or an authorized agent who has express authority to represent the Applicant, and who has authority on behalf of the Applicant to sign Subscriber Agreements.

**Control**: "Control" (and its correlative meanings, "controlled by" and "under common control with") means possession, directly or indirectly, of the power to: (1) direct the management, personnel, finances, or plans of such entity; (2) control the election of a majority of the directors ; or (3) vote that portion of voting shares required for "control" under the law of the entity's Jurisdiction of Incorporation or Registration but in no case less than 10%.

**Country**: Either a member of the United Nations OR a geographic region recognized as a Sovereign State by at least two UN member nations.

**Cross Certificate**: A Certificate that is used to establish a trust relationship between two Root CAs.

**CSPRNG**: A pseudo-random number generator intended for use in a cryptographic system.

**Delegated Third Party**: A natural person or Legal Entity that is not the CA but is authorized by the CA, and whose activities are not within the scope of the appropriate CA audits, to assist in the Certificate Management Process by performing or fulfilling one or more of the CA requirements found herein.

**Digital Identity Document**: a government-issued identity document that is issued in a machine-processable form, that is digitally signed by the issuer, and that is in purely digital form.

**Domain Label**: From [RFC 8499](http://tools.ietf.org/html/rfc8499): "An ordered list of zero or more octets that makes up a portion of a domain name. Using graph theory, a label identifies one node in a portion of the graph of all possible domain names."

**Domain Name**: An ordered list of one or more Domain Labels assigned to a node in the Domain Name System.

**Enterprise RA**: An employee or agent of an organization unaffiliated with the CA who authorizes issuance of Certificates to that organization.

**Expiry Date**: The "Not After" date in a Certificate that defines the end of a Certificate's validity period.

**Fully-Qualified Domain Name**: A Domain Name that includes the Domain Labels of all superior nodes in the Internet Domain Name System.

**Government Entity**: A government-operated legal entity, agency, department, ministry, branch, or similar element of the government of a country, or political subdivision within such country (such as a state, province, city, county, etc.).

**Individual**: A natural person.

**Issuing CA**: In relation to a particular Certificate, the CA that issued the Certificate. This could be either a Root CA or a Subordinate CA.

**Jurisdiction of Incorporation**: In the context of a Private Organization, the country and (where applicable) the state or province or locality where the organization's legal existence was established by a filing with (or an act of) an appropriate government agency or entity (e.g., where it was incorporated). In the context of a Government Entity, the country and (where applicable) the state or province where the Entity's legal existence was created by law.

**Jurisdiction of Registration**: In the case of a Business Entity, the state, province, or locality where the organization has registered its business presence by means of filings by a Principal Individual involved in the business.

**Key Compromise**: A Private Key is said to be compromised if its value has been disclosed to an unauthorized person, or an unauthorized person has had access to it.

**Key Generation Script**: A documented plan of procedures for the generation of a CA Key Pair.

**Key Pair**: The Private Key and its associated Public Key.

**Legacy Profile**: The S/MIME Legacy Profiles provide flexibility for existing reasonable S/MIME certificate practices to become auditable under the S/MIME Baseline Requirements. This includes options for Subject DN attributes, `extKeyUsage`, and other extensions. The Legacy Profiles will be deprecated in a future version of the S/MIME Baseline Requirements.

**Legal Entity**: An association, corporation, partnership, proprietorship, trust, government entity or other entity with legal standing in a country's legal system.

**Mailbox-Validated (MV)**: Refers to a Certificate Profile Subject that is limited to (optional) `subject:emailAddress` and/or `subject:serialNumber` attributes.

**Mailbox Address**: Also Email Address. From [RFC 5321](http://tools.ietf.org/html/rfc5321): "A character string that identifies a user to whom mail will be sent or a location into which mail will be deposited."

**Multipurpose Profile**: The S/MIME Multipurpose Profiles are aligned with the more defined Strict Profiles, but with additional options for `extKeyUsage` and other extensions. This is intended to allow flexibility for crossover use cases between document signing and secure email. 

**Object Identifier**: A unique alphanumeric or numeric identifier registered under the International Organization for Standardization's applicable standard for a specific object or object class.

**OCSP Responder**: An online server operated under the authority of the CA and connected to its Repository for processing Certificate status requests. See also, Online Certificate Status Protocol.

**Online Certificate Status Protocol**: An online Certificate-checking protocol that enables relying-party application software to determine the status of an identified Certificate. See also OCSP Responder.

**Parent Company**: A company that Controls a Subsidiary Company.

**Personal Name**: Personal Name is a name of an Individual Subject typically presented as `subject:givenName` and/or `subject:surname`. However, the Personal Name may be in a format preferred by the Subject, the CA, or Enterprise RA as long as it remains a meaningful representation of the Subject’s verified name.

**Physical Identity Document**: a government-issued identity document issued in physical and human-readable form (such as a passport or national identity card).

**Principal Individual**: An individual of a Private Organization, Government Entity, or Business Entity that is either an owner, partner, managing member, director, or officer, as identified by their title of employment, or an employee, contractor or agent authorized by such entity or organization to conduct business related to the request, issuance, and use of Certificates.

**Private Key**: The key of a Key Pair that is kept secret by the holder of the Key Pair, and that is used to create Digital Signatures and/or to decrypt electronic records or files that were encrypted with the corresponding Public Key.

**Private Organization**: A non-governmental legal entity (whether ownership interests are privately held or publicly traded) whose existence was created by a filing with (or an act of) the Incorporating Agency or equivalent in its Jurisdiction of Incorporation.

**Pseudonym**: A fictitious identity that a person assumes for a particular purpose. Unlike an anonymous identity, a pseudonym can be linked to the person's real identity.

**Public Key**: The key of a Key Pair that can be publicly disclosed by the holder of the corresponding Private Key and that is used by a Relying Party to verify Digital Signatures created with the holder's corresponding Private Key and/or to encrypt messages so that they can be decrypted only with the holder's corresponding Private Key.

**Public Key Infrastructure**: A set of hardware, software, people, procedures, rules, policies, and obligations used to facilitate the trustworthy creation, issuance, management, and use of Certificates and keys based on Public Key Cryptography.

**Publicly-Trusted Certificate**: A Certificate that is trusted by virtue of the fact that its corresponding Root CA Certificate is distributed as a trust anchor in widely-available application software.

**Qualified Auditor**: A natural person or Legal Entity that meets the requirements of [Section 8.2](#82-identityqualifications-of-assessor).

**Qualified Government Information Source**: A database maintained by a Government Entity (e.g. SEC filings) that meets the requirements of [Section 3.2.8.6](#3286-qualified-government-information-source).

**Qualified Government Tax Information Source**: A Qualified Governmental Information Source that specifically contains tax information relating to Private Organizations, Business Entities, or Individuals.

**Qualified Independent Information Source**: A regularly-updated and current, publicly available, database designed for the purpose of accurately providing the information for which it is consulted, and which is generally recognized as a dependable source of such information.

**Random Value**: A value specified by a CA to the Applicant that exhibits at least 112 bits of entropy.

**Registered Domain Name**: A Domain Name that has been registered with a Domain Name Registrar.

**Registration Authority (RA)**: Any Legal Entity that is responsible for identification and authentication of subjects of Certificates, but is not a CA, and hence does not sign or issue Certificates. An RA MAY assist in the certificate application process or revocation process or both. When "RA" is used as an adjective to describe a role or function, it does not necessarily imply a separate body, but can be part of the CA.

**Regulated Professions Information Source**: A Qualified Government Information Source or government-approved database that contains information on information on regulated professions (e.g., where access and exercise of a professional Title is subject to the possession of a specific professional qualification).

**Reliable Method of Communication**: A method of communication, such as a postal/courier delivery address, telephone number, or email address, that was verified using a source other than the Applicant Representative.

**Relying Party**: Any natural person or Legal Entity that relies on a Valid Certificate. An Application Software Supplier is not considered a Relying Party when software distributed by such Supplier merely displays information relating to a Certificate.

**Repository**: An online database containing publicly-disclosed PKI governance documents (such as Certificate Policies and Certification Practice Statements) and Certificate status information, either in the form of a CRL or an OCSP response.

**Requirements**: The S/MIME Baseline Requirements found in this document.

**Root CA**: The top level Certification Authority whose Root CA Certificate is distributed by Application Software Suppliers and that issues Subordinate CA Certificates.

**Root CA Certificate**: The self-signed Certificate issued by the Root CA to identify itself and to facilitate verification of Certificates issued to its Subordinate CAs.

**Signing Authority**: One or more Certificate Approvers designated to act on behalf of the Applicant.

**Sovereign State**: A state or country that administers its own government, and is not dependent upon, or subject to, another power.

**Sponsor-validated**: Refers to a Certificate Profile Subject which combines Individual (natural person) attributes in conjunction with an `subject:organizationName` (an associated Legal Entity) attribute. Registration for Sponsor-validated Certificates MAY be performed by an Enterprise RA where the `subject:organizationName` is either that of the delegated enterprise, or an Affiliate of the delegated enterprise, or that the delegated enterprise is an agent of the named Subject Organization. 

**Strict Profile**: The S/MIME Strict Profiles are the long term target profile for S/MIME Certificates with `extKeyUsage` limited to `emailProtection`, and stricter use of Subject DN attributes and other extensions.

**Subject**: The natural person, device, system, unit, or Legal Entity identified in a Certificate as the Subject. The Subject is either the Subscriber or a mailbox under the control and operation of the Subscriber.

**Subject Identity Information**: Information that identifies the Certificate Subject. Subject Identity Information does not include a Mailbox Address listed in the `subjectAltName` extension, the `subject:commonName` field, or the Subject `subject:emailAddress` field.

**Subordinate CA**: A Certification Authority whose Certificate is signed by the Root CA, or another Subordinate CA.

**Subscriber**: A natural person or Legal Entity to whom a Certificate is issued and who is legally bound by a Subscriber Agreement or Terms of Use.

**Subscriber Agreement**: An agreement between the CA and the Applicant/Subscriber that specifies the rights and responsibilities of the parties.

**Subsidiary Company**: A company that is controlled by a Parent Company.

**Supplementary Evidence**: Used in addition to authoritative evidence to strengthen the reliability of the identity verification and/or as evidence for attributes that are not evidenced by the authoritative evidence.

**Technically Constrained Subordinate CA Certificate**: A Subordinate CA Certificate which uses a combination of Extended Key Usage settings and Name Constraint settings to limit the scope within which the Subordinate CA Certificate MAY issue Certificates to Subscriber or additional Subordinate CAs.

**Terms of Use**: Provisions regarding the safekeeping and acceptable uses of a Certificate issued in accordance with these Requirements when the Applicant/Subscriber is an Affiliate of the CA or is the CA.

**Trustworthy System**: Computer hardware, software, and procedures that are: reasonably secure from intrusion and misuse; provide a reasonable level of availability, reliability, and correct operation; are reasonably suited to performing their intended functions; and enforce the applicable security policy.

**Valid Certificate**: A Certificate that passes the validation procedure specified in [RFC 5280](http://tools.ietf.org/html/rfc5280).

**Validation Specialists**: Someone who performs the information verification duties specified by these Requirements.

**Validity Period**: From [RFC 5280](http://tools.ietf.org/html/rfc5280): "The period of time from notBefore through notAfter, inclusive."

**Verified Accountant Letter**: A document meeting the requirements specified in [Section 3.2.8.2](#3282-verified-accountant-letter).

**Verified Legal Opinion**: A document meeting the requirements specified in [Section 3.2.8.1](#3281-verified-legal-opinion).

**Verified Method of Communication**: The use of a telephone number, a fax number, an email address, or postal delivery address, confirmed by the CA in accordance with [Section 3.2.3.5](#3235-verified-method-of-communication) as a reliable way of communicating with the Applicant.

**Verified Professional Letter**: A Verified Accountant Letter or Verified Legal Opinion.

###  1.6.2 Acronyms

|Acronym   |Meaning                                                            |
|----------|-------------------------------------------------------------------|
|AICPA	|American Institute of Certified Public Accountants |
|CA	   |Certification Authority |
|CAA	   |Certification Authority Authorization |
|CICA	   |Canadian Institute of Chartered Accountants |
|CP	   |Certificate Policy |
|CPS	   |Certification Practice Statement |
|CRL	   |Certificate Revocation List |
|DBA	   |Doing Business As |
|DNS	   |Domain Name System |
|ETSI	   |European Telecommunications Standards Institute |
|FIPS	   |(US Government) Federal Information Processing Standard|
|IANA	   |Internet Assigned Numbers Authority |
|ICANN	|Internet Corporation for Assigned Names and Numbers|
|ICAO	   |International Civil Aviation Organization |
|ISO	   |International Organization for Standardization |
|MV	   |Mailbox-validated |
|NIST	   |(US Government) National Institute of Standards and Technology |
|OCSP	   |Online Certificate Status Protocol |
|OID	   |Object Identifier |
|PKI	   |Public Key Infrastructure |
|RA	   |Registration Authority |
|S/MIME  |Secure MIME (Multipurpose Internet Mail Extensions) |
|TLS	   |Transport Layer Security |

###  1.6.3 References

"EV Guidelines" means the relevant version of the CA/Browser Forum's Guidelines for the Issuance and Management of Extended Validation Certificates". See https://cabforum.org/extended-validation/

"TLS Baseline Requirements" means the relevant version of the CA/Browser Forum's "Baseline Requirements for the Issuance and Management of Publicly‐Trusted TLS Server Certificates". See https://cabforum.org/baseline-requirements-documents/

ETSI TS 119 461, Electronic Signatures and Infrastructures (ESI);. Policy and security requirements for trust service components.

ETSI EN 319 403, Electronic Signatures and Infrastructures (ESI); Trust Service Provider Conformity Assessment - Requirements for conformity assessment bodies assessing Trust Service Providers.

ETSI EN 319 411-1, Electronic Signatures and Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 1: General requirements.

ETSI EN 319 411-2, Electronic Signatures and Infrastructures (ESI); Policy and security requirements for Trust Service Providers issuing certificates; Part 2: Requirements for trust service providers issuing EU qualified certificates.

ETSI EN 319 412-5, Electronic Signatures and Infrastructures (ESI);. Certificate Profiles; Part 5: QCStatements.

ETSI TS 119 172-4, Electronic Signatures and Infrastructures (ESI);. Signature Policies;. Part 4: Signature applicability rules.

FIPS 140-2, Federal Information Processing Standards Publication - Security Requirements For Cryptographic Modules, Information Technology Laboratory, National Institute of Standards and Technology, May 25, 2001.

FIPS 186-4, Federal Information Processing Standards Publication - Digital Signature Standard (DSS), Information Technology Laboratory, National Institute of Standards and Technology, July 2013.

ICAO DOC 9303, Machine Readable Travel Documents, Part 10, Logical Data Structure (LDS) for Storage of Biometrics and Other Data in the Contactless Integrated Circuit (IC), International Civil Aviation Organization, Eighth Edition, 2021.

ICAO DOC 9303, Machine Readable Travel Documents, Part 11, Security Mechanisms for MRTDs, International Civil Aviation Organization, Eighth Edition, 2021.

ISO 17442-1:2020, Financial services — Legal entity identifier (LEI) — Part 1: Assignment.

ISO 17442-2:2020, Financial services — Legal entity identifier (LEI) — Part 2: Application in digital certificates.

ISO 21188:2006, Public key infrastructure for financial services -- Practices and policy framework.

Network and Certificate System Security Requirements, v.1.0, 1/1/2013.

NIST SP 800-89, Recommendation for Obtaining Assurances for Digital Signature Applications.

RFC 2119, Request for Comments: 2119, Key words for use in RFCs to Indicate Requirement Levels, Bradner, March 1997.

RFC 2527, Request for Comments: 2527, Internet X.509 Public Key Infrastructure: Certificate Policy and Certification Practices Framework, Chokhani, et al, March 1999.

RFC 3492, Request for Comments: 3492, Punycode: A Bootstring encoding of Unicode for Internationalized Domain Names in Applications (IDNA). A. Costello. March 2003.

RFC 3647, Request for Comments: 3647, Internet X.509 Public Key Infrastructure: Certificate Policy and Certification Practices Framework, Chokhani, et al, November 2003.

RFC 3739, Request for Comments: 3739, Internet X.509 Public Key Infrastructure: Qualified Certificates Profile, S. Santesson, et al, March 2004.

RFC 3912, Request for Comments: 3912, WHOIS Protocol Specification, Daigle, September 2004.

RFC 3986, Request for Comments: 3986, Uniform Resource Identifier (URI): Generic Syntax. T. Berners-Lee, et al. January 2005.

RFC 3966, Request for Comments: 3966, The tel URI for Telephone Numbers. H. Schulzrinne. December 2004.

RFC 4262, Request for Comments: 4262, X.509 Certificate Extension for Secure/Multipurpose Internet Mail Extensions (S/MIME) Capabilities, S. Santesson, December 2005.

RFC 4366, Request for Comments: 4366, Transport Layer Security (TLS) Extensions, Blake-Wilson, et al, April 2006.

RFC 5019, Request for Comments: 5019, The Lightweight Online Certificate Status Protocol (OCSP) Profile for High-Volume Environments, A. Deacon, et al, September 2007.

RFC 5280, Request for Comments: 5280, Internet X.509 Public Key Infrastructure: Certificate and Certificate Revocation List (CRL) Profile, Cooper et al, May 2008.

RFC 5890, Request for Comments: 5890, Internationalized Domain Names for Applications (IDNA): Definitions and Document Framework. J. Klensin. August 2010.

RFC 5952, Request for Comments: 5952, A Recommendation for IPv6 Address Text Representation. S. Kawamura, et al. August 2010.

RFC 6532. Request for Comments: 6532, Internationalized Email Headers, A. Yang, et al, February 2012.

RFC 6818. Updates to the Internet X.509 Public Key Infrastructure Certificate and Certificate Revocation List (CRL) Profile, January 2013.

RFC 6960, Request for Comments: 6960, X.509 Internet Public Key Infrastructure Online Certificate Status Protocol - OCSP. Santesson, Myers, Ankney, Malpani, Galperin, Adams, June 2013.

RFC 6962, Request for Comments: 6962, Certificate Transparency. B. Laurie, A. Langley, E. Kasper. June 2013.

RFC 7231, Request For Comments: 7231, Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content, R. Fielding, J. Reschke. June 2014.

RFC 7538, Request For Comments: 7538, The Hypertext Transfer Protocol Status Code 308 (Permanent Redirect), J. Reschke. April 2015.

RFC 7482, Request for Comments: 7482, Registration Data Access Protocol (RDAP) Query Format, Newton, et al, March 2015.

RFC 8398, Request for Comments: 8398, Internationalized Email Addresses in X.509 Certificates, MAY 2018. A. Melnikov, et al. May 2018.

RFC 8499, Request for Comments: 8499, DNS Terminology. P. Hoffman, et al. January 2019.

RFC 8659, Request for Comments: 8659, DNS Certification Authority Authorization (CAA) Resource Record, Hallam-Baker, Stradling, Hoffman-Andrews, November 2019.

WebTrust for Certification Authorities.

X.509, Recommendation ITU-T X.509 (10/2012) \| ISO/IEC 9594-8:2014 (E), Information technology – Open Systems Interconnection – The Directory: Public-key and attribute certificate frameworks.


###  1.6.4 Conventions

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in these Requirements shall be interpreted in accordance with [RFC 2119](http://tools.ietf.org/html/rfc2119).

# 2. PUBLICATION AND REPOSITORY RESPONSIBILITIES
The CA SHALL develop, implement, enforce, and annually update a Certificate Policy and/or Certification Practice Statement (CP and/or CPS) that describes in detail how the CA implements the latest version of these Requirements.

## 2.1 Repositories

The CA SHALL make revocation information for Subordinate CA Certificates and Subscriber Certificates available in accordance with this Policy.

## 2.2 Publication of certification information

The CA SHALL publicly disclose its CP and/or CPS through an appropriate and readily accessible online means that is available on a 24x7 basis. The CA SHALL publicly disclose its CA business practices to the extent required by the CA's selected audit scheme (see [Section 8](#8-compliance-audit-and-other-assessments)).

The CP and/or CPS SHALL be structured in accordance with [RFC 3647](http://tools.ietf.org/html/rfc3647) and SHALL include all material required by [RFC 3647](http://tools.ietf.org/html/rfc3647).

The CA SHALL publicly give effect to these Requirements and represent that it will adhere to the latest published version. The CA MAY fulfill this requirement by incorporating these Requirements directly into its CP and/or CPSs or by incorporating them by reference using a clause such as the following (which SHALL include a link to the official version of these Requirements):

> [Name of CA] conforms to the current version of the Baseline Requirements for the Issuance and Management of Publicly-Trusted S/MIME Certificates published at http://www.cabforum.org. In the event of any inconsistency between this document and those Requirements, those Requirements take precedence over this document.

## 2.3 Time or frequency of publication

The CA SHALL develop, implement, enforce, and annually update a CP and/or CPS that describes in detail how the CA implements the latest version of these Requirements. The CA SHALL indicate conformance with this requirement by incrementing the version number and adding a dated changelog entry, even if no other changes are made to the document.

## 2.4 Access controls on repositories

The CA SHALL make its Repository publicly available in a read-only manner.

# 3. IDENTIFICATION AND AUTHENTICATION

## 3.1 Naming

 No stipulation.

### 3.1.1 Types of names

When the `subject:commonName` of a Certificate issued to an Individual does not contain a Mailbox Address, it is specified as a Personal Name or `subject:pseudonym` as described in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields)(a). 

Personal Names MUST be a meaningful representation of the Subject’s name as verified in the identifying documentation or Enterprise RA records. 

Names consisting of multiple words are permitted. Given names joined with a hyphen are considered as one single given name. Subjects with more than one given name MAY choose one or several of their given names in any sequence.  Subjects MAY chose name order in accordance with national preference. 

The CA MAY allow common variations or abbreviations of Personal Names consistent with local practice. 

### 3.1.2 Need for names to be meaningful

No stipulation.

### 3.1.3 Anonymity or pseudonymity of subscribers

The purpose of the `subject:pseudonym` attribute is to provide a unique identifier linked to an Individual in a pseudonymized manner when certain privacy conditions are required. For example, a Pseudonym may be used if a government agency requires officials to sign certain decisions via S/MIME so those decisions trace back to individuals, but emphasize the importance of the role over Individual identity in the Certificate. The CA must disclose in its CP and/or CPS if it allows the use of Pseudonyms.

For `sponsor-validated` certificates, the CA MAY use a `subject:pseudonym` attribute in the Certificate if approved by an Enterprise RA and the associated Subject has been verified according to [Section 3.2.4](#324-authentication-of-individual-identity). If present, the `subject:pseudonym` attribute MUST be: 
  1. either a unique identifier selected by the CA for the Subject of the Certificate; or
  2. an identifier selected by the Enterprise RA which uniquely identifies the Subject of the Certificate within the Organization included in the `subject:organizationName` attribute.

For `individual-validated` certificates, the CA MAY use the `subject:pseudonym` attribute if the associated Subject has been verified according to [Section 3.2.4](#324-authentication-of-individual-identity). If present, the `subject:pseudonym` attribute MUST be: 
  1. either a unique identifier selected by the CA for the Subject of the Certificate; or
  2. an identifier verified based on government-issued identity documents.

Pseudonym Certificates are not anonymous. CAs and Enterprise RAs SHALL treat Individual identity information relating to a Pseudonym as private in accordance with [Section 9.4.2](#942-information-treated-as-private).

### 3.1.4 Rules for interpreting various name forms

In cases where names use diacritics or other characters that are not supported by Relying Party applications, the CA SHOULD define substitution rules in its CP and/or CPS.  For example, regardless of capitalization:

*  Accent characters MAY be represented by their ASCII equivalent. For example é, à, í, ñ, or ç MAY be represented by e, a, i, n, or c.
*  Umlaut-accented characters such as ä, ö, ü MAY be represented by either ae, oe, ue or a, o, u.

### 3.1.5 Uniqueness of names

No stipulation.

### 3.1.6 Recognition, authentication, and role of trademarks

No stipulation.

## 3.2 Initial identity validation

The CA SHALL authenticate the identity attributes of the Subject and their control over the email addresses to be included in the S/MIME Certificate according to the requirements of the following sections:

| Type    | Mailbox Control | Organization Identity | Individual Identity | 
|---------|----------|----------|----------|
| Mailbox-validated | Section 3.2.2  | NA | NA | 
| Organization-validated |  Section 3.2.2  | Section 3.2.3 | NA |
| Sponsored-validated | Section 3.2.2 | Section 3.2.3 | Section 3.2.4 | 
| Individual-validated | Section 3.2.2 | NA | Section 3.2.4 | 

### 3.2.1 Method to prove possession of private key

No stipulation.

### 3.2.2 Validation of mailbox authorization or control

This section defines the permitted processes and procedures for confirming the Applicant's control of the email addresses to be included in issued Certificates. 

The CA SHALL verify that Applicant controls the email accounts associated with all email addresses referenced in the Certificate or has been authorized by the email account holder to act on the account holder’s behalf. 

The CA SHALL NOT delegate the verification of mailbox authorization or control.

**Note:** Email addresses MAY be listed in Subscriber Certificates using `rfc822Name` or `otherNames` of `type id-on-SmtpUTF8Mailbox` in the `subjectAltName` extension, or in Subordinate CA Certificates via `rfc822Name` in permittedSubtrees within the `nameConstraints` extension.

The CA's CP and/or CPS SHALL specify the procedures that the CA employs to perform this verification. CAs SHALL maintain a record of which domain validation method, including the relevant version number from the Baseline Requirements or S/MIME Baseline Requirements, used to validate every domain or email address in issued Certificates.

Completed validations of Applicant authority MAY be valid for the issuance of multiple Certificates over time. In all cases, the validation SHALL have been initiated within the time period specified in the relevant requirement (such as [Section 4.2.1](#421-performing-identification-and-authentication-functions)) prior to Certificate issuance.

#### 3.2.2.1 Validating authority over mailbox via domain

The CA MAY confirm the Applicant, such as an Enterprise RA, has been authorized by the email account holder to act on the account holder’s behalf by verifying the entity's control over the domain portion of the email address to be used in the Certificate.

The CA SHALL use only the approved methods in Section 3.2.2.4 of the TLS Baseline Requirements to perform this verification.

For purposes of domain validation, the term Applicant includes the Applicant's Parent Company, Subsidiary Company, or Affiliate.

#### 3.2.2.2 Validating control over mailbox via email

The CA MAY confirm the Applicant's control over each `rfc822Name` or `otherName` of type `id-on-SmtpUTF8Mailbox` to be included in a Certificate by sending a Random Value via email and then receiving a confirming response utilizing the Random Value. 

Control over each email address SHALL be confirmed using a unique Random Value. The Random Value SHALL be sent only to the email address being validated and SHALL not be shared in any other way. 

The Random Value SHALL be unique in each email. The Random Value SHALL remain valid for use in a confirming response for no more than 24 hours from its creation. The CA MAY specify a shorter validity period for Random Values in its CP and/or CPS.  

The Random Value SHALL be reset upon each instance of the email sent by the CA and, if intended for additional use as an authentication factor, upon first use. 

#### 3.2.2.3 Validating applicant as operator of associated mail server(s)

Confirming the Applicant's control over each `rfc822Name` , `otherName` of `type id-on-SmtpUTF8Mailbox` to be included in the Certificate, by confirming control of the SMTP FQDN to which a message delivered to the email address should be directed. The SMTP FQDN MUST be identified using the address resolution algorithm defined in [RFC 5321 Section 5.1](https://datatracker.ietf.org/doc/html/rfc5321#section-5.1) which determines which SMTP FQDNs are authoritative for a given email address. If more than one SMTP FQDNs have been discovered, the CA MUST verify control of an SMTP FQDN following the selection process at [RFC 5321 Section 5.1](https://datatracker.ietf.org/doc/html/rfc5321#section-5.1). Aliases in MX record RDATA MUST NOT be used for this validation method.

When confirming the Applicant's control of the SMTP FQDN, the CA SHALL use only the approved methods in Section 3.2.2.4 of the TLS Baseline Requirements.

This method is suitable for validating control of all email addresses under a single domain.

#### 3.2.2.4 CAA records

This version of the S/MIME Baseline Requirements does not require the CA to check for CAA records. The CAA property tags for `issue`, `issuewild`, and `iodef` as specified in [RFC 8659](https://datatracker.ietf.org/doc/html/rfc8659) are not recognized for the issuance of S/MIME Certificates.

### 3.2.3 Authentication of organization identity

The following requirements MUST be fulfilled to authenticate Organization identity included in the `Organization-validated` and `Sponsor-validated` Certificate types.

#### 3.2.3.1 Verification requirements – overview

The CA MUST implement verification processes to confirm and document the following requirements associated with the `subject:organizationName` attribute:

1. Verify Applicant's existence and identity, including;

   A.  Verify the Applicant's legal existence and identity;

   B.  Verify the Applicant's physical existence (business presence at a physical address); and

   C.  Verify the Applicant's operational existence (business activity).

2. Verify a reliable means of communication with the entity to be named as the Subject in the Certificate;

3. Verify the Applicant's authorization for the S/MIME Certificate, including;

   A.  Verify the name, title, and authority of the Contract Signer, Certificate Approver, and Certificate Requester,

   B.  Verify that a Contract Signer signed the Subscriber Agreement or that a duly authorized Applicant Representative acknowledged and agreed to the Terms of Use; and

   C.  Verify that a Certificate Approver has signed or otherwise approved the S/MIME Certificate Request.

As a general rule, the CA is responsible for taking all verification steps reasonably necessary to satisfy each of the Verification Requirements set forth in the subsections below. The Acceptable Methods of Verification set forth in [Section 3.2.3](#323-authentication-of-organization-identity) and [Section 3.2.6](#326-validation-of-authority) (which usually include alternatives) are considered to be the minimum acceptable level of verification required of the CA.  In all cases, however, the CA is responsible for taking any additional verification steps that may be reasonably necessary under the circumstances to satisfy the applicable Verification Requirement.

##### 3.2.3.1.1 Disclosure of verification sources

Prior to the use of an Incorporating Agency or Registration Agency to fulfill these verification requirements, the CA MUST publicly disclose Agency Information about the Incorporating Agency or Registration Agency. This disclosure SHALL be through an appropriate and readily accessible online means.

This Agency Information SHALL include at least the following:

* Sufficient information to unambiguously identify the Incorporating Agency or Registration Agency (such as a name, jurisdiction, and website); 
* The accepted value or values for each of the 2 character ISO 3166 country codes and the 2 character ISO 316-2 identifier for the subdivision (state or province) of the `subject:organizationIdentifier` field, when a Certificate is issued using information from that Incorporating Agency or Registration Agency, indicating the jurisdiction(s) that the Agency is appropriate for; 
* The acceptable form or syntax of Registration Numbers used by the Incorporating Agency or Registration Agency, if the CA restricts such Numbers to an acceptable form or syntax; and
* A revision history that includes a unique version number and date of publication for any additions, modifications, and/or removals from this list.

The CA MUST document where to obtain this information within Section 3.2 of the CA's CP and/or CPS.

#### 3.2.3.2 Verification of applicant's legal existence and identity

##### 3.2.3.2.1 Verification requirements

To verify the Applicant's legal existence and identity, the CA MUST do the following.

1. **Private Organization Subjects**

   A.  **Legal Existence**: Verify that the Applicant is a legally recognized entity, in existence and validly formed (e.g., incorporated) with the Incorporating or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration, and not designated on the records of the Incorporating or Registration Agency by labels such as "inactive", "invalid", "not current", or the equivalent.
   B.  **Organization Name**: Verify that the Applicant's formal legal name as recorded with the Incorporating or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration matches the Applicant's name in the S/MIME Certificate Request.
   C.  **Registration Number**: Obtain the specific Registration Number assigned to the Applicant by the Incorporating or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration. Where the Incorporating or Registration Agency does not assign a Registration Number, the CA SHALL obtain the Applicant's date of Incorporation or Registration.
   D.  **Registered Agent**: Obtain the identity and address of the Applicant's Registered Agent or Registered Office (as applicable in the Applicant's Jurisdiction of Incorporation or Registration).

2. **Government Entity Subjects**

   A.  **Legal Existence**: Verify that the Applicant is a legally recognized Government Entity, in existence in the political subdivision in which such Government Entity operates.
   B.  **Entity Name**: Verify that the Applicant's formal legal name matches the Applicant's name in the S/MIME Certificate Request.
   C.  **Registration Number**: The CA MUST attempt to obtain the Applicant's date of incorporation, registration, or formation, or the identifier for the legislative act that created the Government Entity. In circumstances where this information is not available, the CA MUST enter appropriate language to indicate that the Subject is a Government Entity.

3. **Business Entity Subjects**

   A.  **Legal Existence**: Verify that the Applicant is engaged in business under the name submitted by the Applicant in the Application.
   B.  **Organization Name**: Verify that the Applicant's formal legal name as recognized by the Registration Agency in the Applicant's Jurisdiction of Registration matches the Applicant's name in the S/MIME Certificate Request.
   C.  **Registration Number**: Attempt to obtain the specific unique Registration Number assigned to the Applicant by the Registration Agency in the Applicant's Jurisdiction of Registration. Where the Registration Agency does not assign a Registration Number, the CA SHALL obtain the Applicant's date of Registration.
   D.  **Principal Individual**: Verify the identity of the identified Principal Individual.

4. **Non-Commercial Entity Subjects (International Organizations)**

   A.  **Legal Existence**: Verify that the Applicant is a legally recognized International Organization Entity.
   B.  **Entity Name**: Verify that the Applicant's formal legal name matches the Applicant's name in the S/MIME Certificate Request.
   C.  **Registration Number**: The CA MUST attempt to obtain the Applicant's date of formation, or the identifier for the legislative act that created the International Organization Entity. In circumstances where this information is not available, the CA MUST enter appropriate language to indicate that the Subject is an International Organization Entity.

##### 3.2.3.2.2 Acceptable methods of verification

1. **Private Organization Subjects**: Unless verified under subsection (6), all items listed in [Section 3.2.3.2.1](#32321-verification-requirements) (1) MUST be verified directly with, or obtained directly from, the Incorporating or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration. Such verification MAY be through use of a Qualified Government Information Source operated by, or on behalf of, the Incorporating or Registration Agency, or by direct contact with the Incorporating or Registration Agency in person or via mail, email, Web address, or telephone, using an address or phone number obtained directly from the Qualified Government Information Source, Incorporating or Registration Agency, or from a Qualified Independent Information Source.

2. **Government Entity Subjects**: Unless verified under subsection (6), all items listed in [Section 3.2.3.2.1](#32321-verification-requirements) (2) MUST either be verified directly with, or obtained directly from, one of the following:
   i. a Qualified Government Information Source in the political subdivision in which such Government Entity operates;
   ii. a superior governing Government Entity in the same political subdivision as the Applicant (e.g. a Secretary of State may verify the legal existence of a specific State Department), or
   iii. from a judge that is an active member of the federal, state or local judiciary within that political subdivision.

   Any communication from a judge SHALL be verified in the same manner as is used for verifying factual assertions that are asserted by an Attorney as set forth in [Section 3.2.8.1](#3281-verified-legal-opinion).

   Such verification MAY be by direct contact with the appropriate Government Entity in person or via mail, email, Web address, or telephone, using an address or phone number obtained from a Qualified Independent Information Source.

3. **Business Entity Subjects**: Unless verified under subsection (6), Items listed in [Section 3.2.3.2.1](#32321-verification-requirements) (3) (A) through (C) above, MUST be verified directly with, or obtained directly from, the Registration Agency in the Applicant's Jurisdiction of Registration. Such verification MAY be performed by means of a Qualified Government Information Source, a Qualified Governmental Tax Information Source, or by direct contact with the Registration Agency in person or via mail, email, Web address, or telephone, using an address or phone number obtained directly from the Qualified Government Information Source, Qualified Governmental Tax Information Source or Registration Agency, or from a Qualified Independent Information Source. In addition, the CA MUST validate a Principal Individual associated with the Business Entity pursuant to the requirements in subsection (4), below.

4. **Principal Individual**: A Principal Individual associated with the Business Entity MUST be validated in a face-to-face setting. The CA MAY rely upon a face-to-face validation of the Principal Individual performed by the Registration Agency, provided that the CA has evaluated the validation procedure and concluded that it satisfies the requirements for face-to-face validation procedures. Where no face-to-face validation was conducted by the Registration Agency, or the Registration Agency's face-to-face validation procedure does not comply with this Requirement, the CA SHALL perform face-to-face validation.

   A.  **Face-To-Face Validation**: The face-to-face validation MUST be conducted before either an employee of the CA, a Latin Notary, a Notary (or equivalent in the Applicant's jurisdiction), a Lawyer, or Accountant (Third-Party Validator). The Principal Individual(s) MUST present the following documentation (Vetting Documents) directly to the Third-Party Validator:

       i. A Personal Statement that includes the following information:

          1. Full name or names by which a person is, or has been, known (including all other names used);
          2. Residential Address at which he/she can be located;
          3. Date of birth; and
          4. An affirmation that all of the information contained in the Certificate Request is true and correct.

       ii. A current signed government-issued identification document that includes a photo of the Individual and is signed by the Individual such as:

           1. A passport;
           2. A driver's license;
           3. A personal identification card;
           4. A concealed weapons permit; or
           5. A military ID.

       iii. At least two secondary documentary evidences to establish his/her identity that include the name of the Individual, one of which MUST be from a financial institution.

            1. Acceptable financial institution documents include:

               a. A major credit card, provided that it contains an expiration date and it has not expired'
               b. A debit card from a regulated financial institution, provided that it contains an expiration date and it has not expired,
               c. A mortgage statement from a recognizable lender that is less than six months old,
               d. A bank statement from a regulated financial institution that is less than six months old.

            2. Acceptable non-financial documents include:

               a. Recent original utility bills or certificates from a utility company confirming the arrangement to pay for the services at a fixed address (not a mobile/cellular telephone bill),
               b. A copy of a statement for payment of a lease, provided that the statement is dated within the past six months,
               c. A certified copy of a birth certificate,
               d. A local authority tax bill for the current year,
               e. A certified copy of a court order, such as a divorce certificate, annulment papers, or adoption papers.

       The Third-Party Validator performing the face-to-face validation MUST:

         i. Attest to the signing of the Personal Statement and the identity of the signer; and
         ii. Identify the original Vetting Documents used to perform the identification. In addition, the Third-Party Validator MUST attest on a copy of the current signed government-issued photo identification document that it is a full, true, and accurate reproduction of the original.

   B.  **Verification of Third-Party Validator**: The CA MUST independently verify that the Third-Party Validator is a legally-qualified Latin Notary or Notary (or legal equivalent in the Applicant's jurisdiction), lawyer, or accountant in the jurisdiction of the Individual's residency, and that the Third-Party Validator actually did perform the services and did attest to the signature of the Individual.

   C.  **Cross-checking of Information**: The CA MUST obtain the signed and attested Personal Statement together with the attested copy of the current signed government-issued photo identification document. The CA MUST review the documentation to determine that the information is consistent, matches the information in the application, and identifies the Individual. The CA MAY rely on electronic copies of this documentation, provided that:

       i. the CA confirms their authenticity (not improperly modified when compared with the underlying original) with the Third-Party Validator; and
       ii. electronic copies of similar kinds of documents are recognized as legal substitutes for originals under the laws of the CA's jurisdiction.

5. **Non-Commercial Entity Subjects (International Organization)**: Unless verified under subsection (6), all items listed in [Section 3.2.3.2.1](#32321-verification-requirements) (4) MUST be verified either:

   A.  With reference to the constituent document under which the International Organization was formed; or
   B.  Directly with a signatory country's government in which the CA is permitted to do business. Such verification MAY be obtained from an appropriate government agency or from the laws of that country, or by verifying that the country's government has a mission to represent it at the International Organization; or
   C.  Directly against any current list of qualified entities that the CA/Browser Forum may maintain at https://www.cabforum.org
   D.  In cases where the International Organization applying for the S/MIME Certificate is an organ or agency - including a non-governmental organization of a verified International Organization, then the CA MAY verify the International Organization Applicant directly with the verified umbrella International Organization of which the Applicant is an organ or agency.

6. The CA MAY rely on a Verified Professional Letter to establish the Applicant's information listed in (1)-(5) above if:

   i. the Verified Professional Letter includes a copy of supporting documentation used to establish the Applicant's legal existence, such as a certificate of registration, articles of incorporation, operating agreement, statute, or regulatory act, and
   ii. the CA confirms the Applicant's organization name specified in the Verified Professional Letter with a QIIS or QGIS.

#### 3.2.3.3 Verification of applicant's legal existence and identity – assumed name

##### 3.2.3.3.1 Verification requirements

If, in addition to the Applicant's formal legal name, as recorded with the applicable Incorporating Agency or Registration Agency in the Applicant's Jurisdiction of Incorporation or Registration, the Applicant's identity, as asserted in the S/MIME Certificate, is to contain any assumed name (also known as "doing business as", "DBA", or "d/b/a" in the US, and "trading as" in the UK) under which the Applicant conducts business, the CA MUST verify that:

   i. the Applicant has registered its use of the assumed name with the appropriate government agency for such filings in the jurisdiction of its Place of Business (as verified in accordance with the S/MIME Baseline Requirements); and
   ii. that such filing continues to be valid.

##### 3.2.3.3.2 Acceptable methods of verification

To verify any assumed name under which the Applicant conducts business:

1. The CA MAY verify the assumed name through use of a Qualified Government Information Source operated by, or on behalf of, an appropriate government agency in the jurisdiction of the Applicant's Place of Business, or by direct contact with such government agency in person or via mail, email, Web address, or telephone; 
2. The CA MAY verify the assumed name through use of a Qualified Independent Information Source provided that the QIIS has verified the assumed name with the appropriate government agency; or
3. The CA MAY rely on a Verified Professional Letter  that indicates the assumed name under which the Applicant conducts business, the government agency with which the assumed name is registered, and that such filing continues to be valid.

#### 3.2.3.4 Verification of applicant's physical existence

##### 3.2.3.4.1 Address of applicant's place of business

1. **Verification Requirements**: To verify the Applicant's physical existence and business presence, the CA MUST verify that the physical address provided by the Applicant is an address where the Applicant or a Parent/Subsidiary Company conducts business operations (not, for example, a mail drop or P.O. box, or 'care of' (C/O) address, such as an address for an agent of the Organization), and is the address of the Applicant's Place of Business.

2. **Acceptable Methods of Verification**

   A.  **Place of Business in the Country of Incorporation or Registration**

       i. For Applicants whose Place of Business is in the same country as the Applicant's Jurisdiction of Incorporation or Registration and whose Place of Business is NOT the same as that indicated in the relevant Qualified Government Information Source used in [Section 3.2.3.2](#3232-verification-of-applicants-legal-existence-and-identity) to verify legal existence:

          1. For Applicants listed at the same Place of Business address in the current version of either at least one QGIS (other than that used to verify legal existence), QIIS or QTIS, the CA MUST confirm that the Applicant's address, as listed in the S/MIME Certificate Request, is a valid business address for the Applicant or a Parent/Subsidiary Company by reference to such QGIS, QIIS, or QTIS, and MAY rely on the Applicant's representation that such address is its Place of Business;

          2. For Applicants who are not listed at the same Place of Business address in the current version of either at least one QIIS or QTIS, the CA MUST confirm that the address provided by the Applicant in the S/MIME Certificate Request is the Applicant's or a Parent/Subsidiary Company's business address, by obtaining documentation of a site visit to the business address, which MUST be performed by a reliable individual or firm. The documentation of the site visit MUST:

             a. Verify that the Applicant's business is located at the exact address stated in the S/MIME Certificate Request (e.g., via permanent signage, employee confirmation, etc.),
             b. Identify the type of facility (e.g., office in a commercial building, private residence, storefront, etc.) and whether it appears to be a permanent business location,
             c. Indicate whether there is a permanent sign (that cannot be moved) that identifies the Applicant,
             d. Indicate whether there is evidence that the Applicant is conducting ongoing business activities at the site (not that it is just, for example, a mail drop, P.O. box, etc.), and
             e. Include one or more photos of
                i. the exterior of the site (showing signage indicating the Applicant's name, if present, and showing the street address if possible), and
                ii. the interior reception area or workspace.

       ii. For all Applicants, the CA MAY alternatively rely on a Verified Professional Letter that indicates the address of the Applicant's or a Parent/Subsidiary Company's Place of Business and that business operations are conducted there.
       iii. For Government Entity Applicants, the CA MAY rely on the address contained in the records of the QGIS in the Applicant's jurisdiction.
       iv. For Applicants whose Place of Business is in the same country as the Applicant's Jurisdiction of Incorporation or Registration and where the QGIS used in [Section 3.2.3.2](#3232-verification-of-applicants-legal-existence-and-identity)  to verify legal existence contains a business address for the Applicant, the CA MAY rely on the address in the QGIS to confirm the Applicant's or a Parent/Subsidiary Company's address as listed in the S/MIME Certificate Request, and MAY rely on the Applicant's representation that such address is its Place of Business.

   B.  **Place of Business not in the Country of Incorporation or Registration**: The CA MUST rely on a Verified Professional Letter that indicates the address of the Applicant's Place of Business and that business operations are conducted there.

#### 3.2.3.5 Verified method of communication

##### 3.2.3.5.1 Verification requirements

To assist in communicating with the Applicant and confirming that the Applicant is aware of and approves issuance, the CA MUST verify a telephone number, fax number, email address, or postal delivery address as a Verified Method of Communication with the Applicant.

##### 3.2.3.5.2 Acceptable methods of verification

To verify a Verified Method of Communication with the Applicant, the CA MUST:

A.  Verify that the Verified Method of Communication belongs to the Applicant, or a Parent/Subsidiary or Affiliate of the Applicant, by matching it with one of the Applicant's Parent/Subsidiary or Affiliate's Places of Business in:

  i. records provided by the applicable phone company;
  ii. a QGIS, QTIS, or QIIS; or
  iii. a Verified Professional Letter; and

B.  Confirm the Verified Method of Communication by using it to obtain an affirmative response sufficient to enable a reasonable person to conclude that the Applicant, or a Parent/Subsidiary or Affiliate of Applicant, can be contacted reliably by using the Verified Method of Communication.

#### 3.2.3.6 Verification of applicant's operational existence

##### 3.2.3.6.1 Verification requirements

The CA MUST verify that the Applicant has the ability to engage in business by verifying the Applicant's, or Affiliate/Parent/Subsidiary Company's, operational existence. The CA MAY rely on its verification of a Government Entity's legal existence under [Section 3.2.3.2](#3232-verification-of-applicants-legal-existence-and-identity) as verification of a Government Entity's operational existence.

##### 3.2.3.6.2 Acceptable methods of verification

To verify the Applicant's ability to engage in business, the CA MUST verify the operational existence of the Applicant, or its Affiliate/Parent/Subsidiary Company, by:

1. Verifying that the Applicant, Affiliate, Parent Company, or Subsidiary Company has been in existence for at least three years, as indicated by the records of an Incorporating Agency or Registration Agency;

2. Verifying that the Applicant, Affiliate, Parent Company, or Subsidiary Company is listed in either a current QIIS or QTIS;

3. Verifying that the Applicant, Affiliate, Parent Company, or Subsidiary Company has an active current Demand Deposit Account with a Regulated Financial Institution by receiving authenticated documentation of the Applicant's, Affiliate's, Parent Company's, or Subsidiary Company's Demand Deposit Account directly from a Regulated Financial Institution; or

4. Relying on a Verified Professional Letter to the effect that the Applicant has an active current Demand Deposit Account with a Regulated Financial Institution.

### 3.2.4 Authentication of individual identity

The following requirements MUST be fulfilled to authenticate Individual identity attributes included in `Sponsor-validated` and `Individual-validated` Certificate profiles.

The CA or RA MUST collect and retain evidence supporting the following identity attributes for the Individual Applicant:

1. Given name(s) and surname(s) (if used), which SHOULD be current names;
2. Pseudonym (if used); 
3. Address (if displayed in Subject); and
4. Further information as needed to uniquely identify the Applicant.

The CA or RA MUST comply with applicable data protection legislation in the gathering and retention of evidence relating to Individual identity supporting this Requirement.

#### 3.2.4.1 Attribute collection of individual identity

The CA MUST document and publish the methods it uses to collect Individual identity attributes.

1.	**From a physical identity document** 

If physical identity documents are used as evidence, the CA or RA SHALL accept only government-issued passports or identity cards, and other official identity documents of comparable reliability (such as drivers license or military ID). 

The physical identity document used as evidence MUST contain a face photo and/or other information that can be compared with the Applicant's physical appearance.

The CA MUST document and publish information describing the physical or digital identity documents or document types it accepts.

2.	**From a digital identity document** 

If digital identity documents (such as passports or national ID cards including a chip bearing digitally signed information about the holder) are used as evidence, the CA or RA SHALL only accept eMRTD digital identity documents according to ICAO 9303 part 10.

This method does not include "eID" as described in Regulation (EU) 910/2014.

3.	**From a certificate supporting a digital signature applied by the Applicant** 

If a digital signature is to be used as evidence, the CA SHALL have the Applicant digitally sign the Certificate Request using a valid personal Certificate that was issued under one of the following adopted standards: eIDAS Qualified Certificates as defined in ETSI EN 319 411-2 and validated according to ETSI TS 119 172-4, IGTF, Adobe Signing Certificate issued under the AATL or CDS program, the Kantara identity assurance framework at level 2, NIST SP 800-63 at level 2, or the FBCA CP at Basic or higher assurance.

The CA SHOULD consider requirements to avoid issuance of a consecutive Certificates that are issued based on a preceding Certificate, where the original verification of the Subject's identity may have been conducted in the distant past.

4.	**From Enterprise RA records** 

In the case of `Sponsor-validated` Certificates approved by an Enterprise RA, records maintained by the Enterprise RA SHALL be accepted as evidence of Individual identity. 

The Enterprise RA MUST maintain records to satisfy the requirements of [Section 1.3.2](#132-registration-authorities) and [Section 8.8](#88-review-of-enterprise-ra-or-technically-constrained-subordinate-ca).

5. **From a verified legal opinion** 

Evidence for Individual identity attributes MAY be gathered using a Verified Legal Opinion.

6. **From authorized reference sources as supplementary evidence** 
   
Evidence for Individual identity attributes SHALL use at least one of the following sources for authoritative evidence:  a physical or digital identity document, digital signature supported by certificate, Enterprise RA records, or a Verified Legal Opinion.

The CA or RA MAY additionally gather and verify supplementary evidence using authorized reference sources such as additional official documents, QGIS, GTIS, Regulated Professions Information Source, or national population registers.

Examples of this method include:

* If the Subject presents an ID featuring an Applicant name that has subsequently been changed, the evidence MAY be complemented by inspection of an official document such as a marriage certificate or court order documenting the change.
* If a professional title of a regulated profession in the`subject:country` is to be used it SHALL be verified against a Regulated Professions Information Source as described in [Section 3.2.8.8](#3288-regulated-professions-information-source).

When external registers are used, the CA or RA SHALL only accept official national or nationally approved registers. The CA SHALL document and publish the accepted authorized registers and reference sources, including a list of the documents or attestations accepted as supplementary evidence of identity.

#### 3.2.4.2 Validation of individual identity

The CA or RA SHALL validate all identity attributes of the Individual to be included in the Certificate.

If the evidence has an explicit validity period, the CA SHALL verify that the time of the identity validation is within this validity period. In context this can include the `validFrom` and `validTo` attributes of a digital signature Certificate or the date of expiry of an identity document.

The CA or RA MAY reuse existing evidence to validate Individual identity subject to the age restrictions in [Section 4.2.1](#421-performing-identification-and-authentication-functions).

1.	**Validation of a physical identity document** 

The physical identity document MUST be presented in its original form. The CA MUST employ procedures to ensure presented by the Applicant is a genuine identity document that is not counterfeited or falsified/modified.

The CA or RA MAY use manual (in person) or remote procedures. A remote process SHALL ensure that the Applicant has the document in hand and presents the document in real-time in front of a camera.

The CA or RA registration agent MUST make a visual comparison of the physical appearance of the Applicant and the face photo and/or other information on the physical identity document.

The CA or RA registration agent SHALL have access to authoritative sources of information on document appearance and validation for forms of identity document accepted by the CA.  

The CA or RA MUST retain information sufficient to evidence the fulfillment of the identity validation process and the verified attributes. In addition to identity attributes, the CA or RA SHALL record the following information: issuer, validity period, and the document's unique identification number.

Automated and manual processes MAY be used in combination, (for example the CA or RA may deploy automated tools to support the work of a registration agent, or an automated process that falls back to a registration agent if the process yields an uncertain result).

2.	**Validation of a digital identity document**

The CA or RA SHALL only accept digital identity documents if the issuer's digital signature on the document is successfully validated according to ICAO 9303 part 11.

The CA or RA SHALL record information obtained from the digital identity document to evidence the identity proofing process. In addition to identity attributes and face photo, the following information SHALL be recorded: issuer, validity period, and the document's unique identification number.

The CA or RA registration agent MUST make a visual comparison of the physical appearance of the Applicant and the face photo and/or other information on the digital identity document.

Automated and manual processes MAY be used in combination, (for example using automated tools to support the work of a registration agent, or an automated process that falls back to a registration agent if the process yields an uncertain result).

3.	**Validation of digital signature with certificate** 

If a digital signature with Certificate is used as evidence, the signature MUST be created as part of the identity validation process.

The CA or RA MUST validate the digital signature and SHALL only use the signing Certificate as evidence for identity attributes if the signature is valid.

If required identity attributes to be collected are not present in the Certificate, the CA or RA SHALL collect these attributes from other sources and validated.

4.	**Validation of a verified legal opinion**

If a Verified Legal Opinion is used as evidence for the validation of Individual identity attributes, then the reliability of the Verified Legal Opinion MUST be verified according to [Section 3.2.8.1](#3281-verified-legal-opinion).

### 3.2.5 Non-verified subscriber information

Subscriber information that has not been verified in accordance with these Requirements SHALL NOT be included in Publicly-Trusted S/MIME Certificates.

### 3.2.6 Validation of authority

If the Certificate Request corresponds to a `Organization-validated` or `Sponsor-validated` Certificate, then for both the Contract Signer and the Certificate Approver, the CA MUST verify the following:

1. **Name, Title and Agency**: The CA MUST verify the name and title of the Contract Signer and the Certificate Approver, as applicable. The CA MUST also verify that the Contract Signer and the Certificate Approver are agents representing the Applicant.
2. **Signing Authority of Contract Signer**: The CA MUST verify that the Contract Signer is authorized by the Applicant to enter into the Subscriber Agreement (and any other relevant contractual obligations) on behalf of the Applicant, including a contract that designates one or more Certificate Approvers on behalf of the Applicant.
3. **Authority of Certificate Approver**: The CA MUST verify, through a source other than the Certificate Approver him- or herself, that the Certificate Approver is expressly authorized by the Applicant to do the following, as of the date of the Certificate Request:

   A.  Submit, and, if applicable, authorize a Certificate Requester to submit, the Certificate Request on behalf of the Applicant; and
   B.  Provide, and, if applicable, authorize a Certificate Requester to provide, the information requested from the Applicant by the CA for issuance of the  Certificate; and
   C.  Approve Certificate Requests submitted by a Certificate Requester.

#### 3.2.6.1 Acceptable methods of verification – name, title and agency

1. **Name and Title**: The CA MAY verify the name and title of the Contract Signer and the Certificate Approver by any appropriate method designed to provide reasonable assurance that a person claiming to act in such a role is in fact the named person designated to act in such role.

2. **Agency**: The CA MAY verify the agency of the Contract Signer and the Certificate Approver by:

   A.  Contacting the Applicant using a Verified Method of Communication for the Applicant, and obtaining confirmation that the Contract Signer and/or the Certificate Approver, as applicable, is an employee;
   B.  Obtaining an Independent Confirmation From the Applicant (as described in [Section 3.2.8.4](#3284-independent-confirmation-from-applicant)), or a Verified Professional Letter verifying that the Contract Signer and/or the Certificate Approver, as applicable, is either an employee or has otherwise been appointed as an agent of the Applicant; or
   C.  Obtaining confirmation from a QIIS or QGIS that the Contract Signer and/or Certificate Approver is an employee of the Applicant.

   The CA MAY also verify the agency of the Certificate Approver via a certification from the Contract Signer (including in a contract between the CA and the Applicant signed by the Contract Signer), provided that the employment or agency status and Signing Authority of the Contract Signer has been verified.

#### 3.2.6.2 Acceptable methods of verification – authority

Acceptable methods of verification of the Signing Authority of the Contract Signer, and the Authority of the Certificate Approver, as applicable, include:

1. **Verified Professional Letter**: The Signing Authority of the Contract Signer, and/or the Authority of the Certificate Approver, MAY be verified by reliance on a Verified Professional Letter;
2. **Corporate Resolution**: The Signing Authority of the Contract Signer, and/or the Authority of the Certificate Approver, MAY be verified by reliance on a properly authenticated corporate resolution that confirms that the person has been granted such Signing Authority, provided that such resolution is

   i. certified by the appropriate corporate officer (e.g., secretary), and
   ii. the CA can reliably verify that the certification was validly signed by such person, and that such person does have the requisite authority to provide such certification;

3. **Independent Confirmation from Applicant**: The Signing Authority of the Contract Signer, and/or the Authority of the Certificate Approver, MAY be verified by obtaining an Independent Confirmation from the Applicant (as described in [Section 3.2.8.4](#3284-independent-confirmation-from-applicant));
4. **Contract between CA and Applicant**: The Authority of the Certificate Approver MAY be verified by reliance on a contract between the CA and the Applicant that designates the Certificate Approver with such Authority, provided that the contract is signed by the Contract Signer and provided that the agency and Signing Authority of the Contract Signer have been verified;
5. **Prior Equivalent Authority**: The signing authority of the Contract Signer, and/or the authority of the Certificate Approver, MAY be verified by relying on a demonstration of Prior Equivalent Authority.

   A.  Prior Equivalent Authority of a Contract Signer MAY be relied upon for confirmation or verification of the signing authority of the Contract Signer when the Contract Signer has executed a binding contract between the CA and the Applicant with a legally valid and enforceable seal or handwritten signature and only when the contract was executed more than 90 days prior to the Certificate application. The CA MUST record sufficient details of the previous agreement to correctly identify it and associate it with the application. Such details MAY include any of the following:

       i. Agreement title;
       ii. Date of Contract Signer's signature;
       iii. Contract reference number; and
       iv. Filing location.

   B.  Prior Equivalent Authority of a Certificate Approver MAY be relied upon for confirmation or verification of the Authority of the Certificate Approver when the Certificate Approver has performed one or more of the following:

       i. Under contract to the CA, has served (or is serving) as an Enterprise RA for the Applicant; or
       ii. Has participated in the approval of one or more Certificate Requests, for Certificates issued by the CA and which are currently and verifiably in use by the Applicant. In this case the CA MUST have contacted the Certificate Approver by phone at a previously validated phone number or have accepted a signed and notarized letter approving the Certificate Request.

6. **QIIS or QGIS**: The Signing Authority of the Contract Signer, and/or the Authority of the Certificate Approver, MAY be verified by a QIIS or QGIS that identifies the Contract Signer and/or the Certificate Approver as a corporate officer, sole proprietor, or other senior official of the Applicant.

7. **Contract Signer's Representation/Warranty**: Provided that the CA verifies that the Contract Signer is an employee or agent of the Applicant, the CA MAY rely on the signing authority of the Contract Signer by obtaining a duly executed representation or warranty from the Contract Signer that includes the following acknowledgments:

   A.  That the Applicant authorizes the Contract Signer to sign the Subscriber Agreement on the Applicant's behalf;
   B.  That the Subscriber Agreement is a legally valid and enforceable agreement;
   C.  That, upon execution of the Subscriber Agreement, the Applicant will be bound by all of its terms and conditions;
   D.  That serious consequences attach to the misuse of a Certificate; and
   E.  The contract signer has the authority to obtain the digital equivalent of a corporate seal, stamp or officer's signature to approve the issuance of S/MIME Certificates on behalf of the Applicant.

#### 3.2.6.3 Pre-authorized certificate approver

Where the CA and Applicant contemplate the submission of multiple future Certificate Requests, then, after the CA:

1. Has verified the name and title of the Contract Signer and that he/she is an employee or agent of the Applicant; and

2. Has verified the Signing Authority of such Contract Signer in accordance with one of the procedures in [Section 3.2.6.2](#3262-acceptable-methods-of-verification--authority).

The CA and the Applicant MAY enter into a written agreement, signed by the Contract Signer on behalf of the Applicant, whereby, for a specified term, the Applicant expressly authorizes one or more Certificate Approver(s) designated in such agreement to exercise Authority with respect to each future Certificate Request submitted on behalf of the Applicant and properly authenticated as originating with, or otherwise being approved by, such Certificate Approver(s).

Such an agreement MUST provide that the Applicant SHALL be obligated under the Subscriber Agreement for all Certificates issued at the request of, or approved by, such Certificate Approver(s) until such Authority is revoked, and MUST include mutually agreed-upon provisions for:

   i. authenticating the Certificate Approver when Certificate Requests are approved,
   ii. periodic re-confirmation of the Authority of the Certificate Approver,
   iii. secure procedures by which the Applicant can notify the CA that the Authority of any such Certificate Approver is revoked, and
   iv. such other appropriate precautions as are reasonably necessary.

### 3.2.7 Criteria for interoperation

The CA SHALL disclose all Cross Certificates that identify the CA as the Subject, provided that the CA arranged for or accepted the establishment of the trust relationship (i.e. the Cross Certificate at issue).

### 3.2.8 Reliability of verification sources

Before relying on a source of verification data to validate Certificate Requests, the CA SHALL verify the reliability of the verification source according to the type of verification source as described in this section.

### 3.2.8.1 Verified legal opinion

1. **Verification Requirements**: Before relying on a legal opinion submitted to the CA, the CA MUST verify that such legal opinion meets the following requirements:

   A.  **Status of Author**: The CA MUST verify that the legal opinion is authored by an independent legal practitioner retained by and representing the Applicant (or an in-house legal practitioner employed by the Applicant) (Legal Practitioner) who is either:

       i. A lawyer (or solicitor, barrister, advocate, or equivalent) licensed to practice law in the applicable jurisdiction. In the case where the Verified Legal Opinion is being used as evidence for the validation of Individual identity attributes as described in [Section 3.2.4.2](#3242-validation-of-individual-identity), the Legal Practitioner MUST be licensed in the jurisdiction where the Individual resides. In all other cases, the Legal Practitioner MUST be licensed in the country of the Applicant's Jurisdiction of Incorporation or Registration or any jurisdiction where the Applicant maintains an office or physical facility, or
       ii. A Latin Notary who is currently commissioned or licensed to practice in the applicable jurisdiction and that jurisdiction recognizes the role of the Latin Notary. In the case where the Latin Notary is providing evidence for the validation of Individual identity attributes as described in [Section 3.2.4.2](#3242-validation-of-individual-identity), the Latin Notary MUST be licensed in the jurisdiction where the Individual resides. In all other cases, the Latin Notary MUST be licensed in country of the Applicant's Jurisdiction of Incorporation or Registration or any jurisdiction where the Applicant maintains an office or physical facility;

   B.  **Basis of Opinion**: The CA MUST verify that the Legal Practitioner is acting on behalf of the Applicant and that the conclusions of the Verified Legal Opinion are based on the Legal Practitioner's stated familiarity with the relevant facts and the exercise of the Legal Practitioner's professional judgment and expertise;
   C.  **Authenticity**: The CA MUST confirm the authenticity of the Verified Legal Opinion.

2. **Acceptable Methods of Verification**: Acceptable methods of establishing the foregoing requirements for a Verified Legal Opinion are:

   A.  **Status of Author**: The CA MUST verify the professional status of the author of the legal opinion by directly contacting the authority responsible for registering or licensing such Legal Practitioner(s) in the applicable jurisdiction;
   B.  **Basis of Opinion**: The text of the legal opinion MUST make it clear that the Legal Practitioner is acting on behalf of the Applicant and that the conclusions of the legal opinion are based on the Legal Practitioner's stated familiarity with the relevant facts and the exercise of the practitioner's professional judgment and expertise. The legal opinion MAY also include disclaimers and other limitations customary in the Legal Practitioner's jurisdiction, provided that the scope of the disclaimed responsibility is not so great as to eliminate any substantial risk (financial, professional, and/or reputational) to the Legal Practitioner, should the legal opinion prove to be erroneous;
   C.  **Authenticity**: To confirm the authenticity of the legal opinion, the CA MUST make a telephone call or send a copy of the legal opinion back to the Legal Practitioner at the address, phone number, facsimile, or (if available) email address for the Legal Practitioner listed with the authority responsible for registering or licensing such Legal Practitioner, and obtain confirmation from the Legal Practitioner or the Legal Practitioner's assistant that the legal opinion is authentic. If a phone number is not available from the licensing authority, the CA MAY use the number listed for the Legal Practitioner in records provided by the applicable phone company, QGIS, or QIIS.

       In circumstances where the opinion is digitally signed, in a manner that confirms the authenticity of the document and the identity of the signer, as verified by the CA in [Section 3.2.8.1](#3281-verified-legal-opinion) (2)(A), no further verification of authenticity is required.

### 3.2.8.2 Verified accountant letter

1. **Verification Requirements**: Before relying on an accountant letter submitted to the CA, the CA MUST verify that such accountant letter meets the following requirements:

   A.  **Status of Author**: The CA MUST verify that the accountant letter is authored by an Accounting Practitioner retained or employed by the Applicant and licensed within the country of the Applicant's Jurisdiction of Incorporation, Jurisdiction of Registration, or country where the Applicant maintains an office or physical facility. Verification of license MUST be  through the member organization or regulatory organization in the Accounting Practitioner's country or jurisdiction that is appropriate to contact when verifying an accountant's license to practice in that country or jurisdiction. Such country or jurisdiction MUST have an accounting standards body that maintains full membership status with the International Federation of Accountants.
   B.  **Basis of Opinion**: The CA MUST verify that the Accounting Practitioner is acting on behalf of the Applicant and that the conclusions of the Verified Accountant Letter are based on the Accounting Practitioner's stated familiarity with the relevant facts and the exercise of the Accounting Practitioner's professional judgment and expertise;
   C.  **Authenticity**: The CA MUST confirm the authenticity of the Verified Accountant Letter.

2. **Acceptable Methods of Verification**: Acceptable methods of establishing the foregoing requirements for a Verified Accountant Letter are listed here.

   A.  **Status of Author**: The CA MUST verify the professional status of the author of the accountant letter by directly contacting the authority responsible for registering or licensing such Accounting Practitioners in the applicable jurisdiction.
   B.  **Basis of Opinion**: The text of the Verified Accountant Letter MUST make clear that the Accounting Practitioner is acting on behalf of the Applicant and that the information in the letter is based on the Accounting Practitioner's stated familiarity with the relevant facts and the exercise of the practitioner's professional judgment and expertise. The Verified Accountant Letter MAY also include disclaimers and other limitations customary in the Accounting Practitioner's jurisdiction, provided that the scope of the disclaimed responsibility is not so great as to eliminate any substantial risk (financial, professional, and/or reputational) to the Accounting Practitioner, should the Verified Accountant Letter prove to be erroneous;
   C.  **Authenticity**: To confirm the authenticity of the accountant's opinion, the CA MUST make a telephone call or send a copy of the Verified Accountant Letter back to the Accounting Practitioner at the address, phone number, facsimile, or (if available) email address for the Accounting Practitioner listed with the authority responsible for registering or licensing such Accounting Practitioners and obtain confirmation from the Accounting Practitioner or the Accounting Practitioner's assistant that the accountant letter is authentic. If a phone number is not available from the licensing authority, the CA MAY use the number listed for the Accountant in records provided by the applicable phone company, QGIS, or QIIS.

      In circumstances where the opinion is digitally signed, in a manner that confirms the authenticity of the document and the identity of the signer, as verified by the CA in [Section 3.2.8.2](#3282-verified-accountant-letter) (2)(A), no further verification of authenticity is required.

### 3.2.8.3 Face-to-face validation

1. **Verification Requirements**: Before relying on face-to-face vetting documents submitted to the CA, the CA MUST verify that the Third-Party Validator meets the following requirements:

   A.  **Qualification of Third-Party Validator**: The CA MUST independently verify that the Third-Party Validator is a legally-qualified Latin Notary or Notary (or legal equivalent in the Applicant's jurisdiction), Lawyer, or Accountant in the jurisdiction of the individual's residency;
   B.  **Document Chain of Custody**: The CA MUST verify that the Third-Party Validator viewed the Vetting Documents in a face-to-face meeting with the individual being validated;
   C.  **Verification of Attestation**: If the Third-Party Validator is not a Latin Notary, then the CA MUST confirm the authenticity of the attestation and vetting documents.

2. **Acceptable Methods of Verification**: Acceptable methods of establishing the foregoing requirements for vetting documents are:

   A.  **Qualification of Third-Party Validator**: The CA MUST verify the professional status of the Third-Party Validator by directly contacting the authority responsible for registering or licensing such Third-Party Validators in the applicable jurisdiction;
   B.  **Document Chain of Custody**: The Third-Party Validator MUST submit a statement to the CA which attests that they obtained the Vetting Documents submitted to the CA for the Individual during a face-to-face meeting with the Individual;
   C.  **Verification of Attestation**: If the Third-Party Validator is not a Latin Notary, then the CA MUST confirm the authenticity of the vetting documents received from the Third-Party Validator. The CA MUST make a telephone call to the Third-Party Validator and obtain confirmation from them or their assistant that they performed the face-to-face validation. The CA MAY rely upon self-reported information obtained from the Third-Party Validator for the sole purpose of performing this verification process. In circumstances where the attestation is digitally signed, in a manner that confirms the authenticity of the documents, and the identity of the signer as verified by the CA in [Section 3.2.8.3](#3283-face-to-face-validation) (1)(A), no further verification of authenticity is required.

### 3.2.8.4 Independent confirmation From applicant

An Independent Confirmation from the Applicant is a confirmation of a particular fact (e.g., confirmation of the employee or agency status of a Contract Signer or Certificate Approver, confirmation of the Authority of a Certificate Approver, etc.) that is:

A.  Received by the CA from a Confirming Person (someone other than the person who is the subject of the inquiry) that has the appropriate authority to confirm such a fact, and who represents that he/she has confirmed such fact;
B.  Received by the CA in a manner that authenticates and verifies the source of the confirmation; and
C.  Binding on the Applicant.

An Independent Confirmation from the Applicant MAY be obtained via the following procedure:

1. **Confirmation Request**: The CA MUST initiate a Confirmation Request via an appropriate out-of-band communication, requesting verification or confirmation of the particular fact at issue as follows:

   A.  **Addressee**: The Confirmation Request MUST be directed to:

       i. A position within the Applicant's organization that qualifies as a Confirming Person (e.g., Secretary, President, CEO, CFO, COO, CIO, CSO, Director, etc.) and is identified by name and title in a current QGIS, QIIS, QTIS, Verified Legal Opinion, Verified Accountant Letter, or by contacting the Applicant using a Verified Method of Communication; or
       ii. The Applicant's Registered Agent or Registered Office in the Jurisdiction of Incorporation as listed in the official records of the Incorporating Agency, with instructions that it be forwarded to an appropriate Confirming Person; or
       iii. A named Individual verified to be in the direct line of management above the Contract Signer or Certificate Approver by contacting the Applicant's Human Resources Department by phone or mail (at the phone number or address for the Applicant's Place of Business, verified in accordance with these Guidelines).

   B.  **Means of Communication**: The Confirmation Request MUST be directed to the Confirming Person in a manner reasonably likely to reach such person. The following options are acceptable:

       i. By paper mail addressed to the Confirming Person at:

          1. The address of the Applicant's Place of Business as verified by the CA in accordance with these Guidelines; or
          2. The business address for such Confirming Person specified in a current QGIS, QTIS, QIIS, Verified Professional Letter; or
          3. The address of the Applicant's Registered Agent or Registered Office listed in the official records of the Jurisdiction of Incorporation, or

       ii. By email addressed to the Confirming Person at the business email address for such person listed in a current QGIS, QTIS, QIIS, Verified Legal Opinion, or Verified Accountant Letter; or
       iii. By telephone call to the Confirming Person, where such person is contacted by calling the main phone number of the Applicant's Place of Business (verified in accordance with these Guidelines) and asking to speak to such person, and a person taking the call identifies him- or herself as such person; or
       iv. By facsimile to the Confirming Person at the Place of Business. The facsimile number MUST be listed in a current QGIS, QTIS, QIIS, Verified Legal Opinion, or Verified Accountant Letter. The cover page MUST be clearly addressed to the Confirming Person.

2. **Confirmation Response**: The CA MUST receive a response to the Confirmation Request from a Confirming Person that confirms the particular fact at issue. Such response MAY be provided to the CA by telephone, by email, or by paper mail, so long as the CA can reliably verify that it was provided by a Confirming Person in response to the Confirmation Request.

3. The CA MAY rely on a verified Confirming Person to confirm their own contact information: email address, telephone number, and facsimile number. The CA MAY rely on this verified contact information for future correspondence with the Confirming Person if:

   A.  The domain of the email address is owned by the Applicant and is the Confirming Person's own email address and not a group email alias;
   B.  The Confirming Person's telephone/fax number is verified by the CA to be a telephone number that is part of the organization's telephone system, and is not the personal phone number for the person.

### 3.2.8.5 Qualified independent information source

A Qualified Independent Information Source (QIIS) is a regularly-updated and publicly available database that is generally recognized as a dependable source for certain information. A database qualifies as a QIIS if the CA determines that:

1. Industries other than the CA sector rely on the database for accurate location, contact, or other information; and

2. The database provider updates its data on at least an annual basis.

The CA SHALL use a documented process to check the accuracy of the database and ensure its data is acceptable, including reviewing the database provider's terms of use. The CA SHALL NOT use any data in a QIIS that the CA knows is

1.  Self-reported; and
2.  Not verified by the QIIS as accurate.

Databases in which the CA or its owners or Affiliated companies maintain a controlling interest, or in which any Registration Authorities or subcontractors to whom the CA has outsourced any portion of the vetting process (or their owners or Affiliated companies) maintain any ownership or beneficial interest, do not qualify as a QIIS.

### 3.2.8.6 Qualified government information source

A Qualified Government Information Source (QGIS) is a regularly-updated and current, publicly available, database designed for the purpose of accurately providing the information for which it is consulted, and which is generally recognized as a dependable source of such information provided that it is maintained by a Government Entity, the reporting of data is required by law, and false or misleading reporting is punishable with criminal or civil penalties. Nothing in these Guidelines prohibits the use of third-party vendors to obtain the information from the Government Entity provided that the third party obtains the information directly from the Government Entity.

### 3.2.8.7 Qualified government tax information source

A Qualified Government Tax Information Source is a Qualified Government Information Source that specifically contains tax information relating to Private Organizations, Business Entities or Individuals (e.g., the IRS in the United States).

### 3.2.8.8 Regulated professions information source

A Regulated Professions Information Source is a Qualified Government Information Source or other government-approved, regularly-updated, and publicly available database that contains information on information on regulated professions (e.g., where access and exercise of a professional Title is subject to the possession of a specific professional qualification).

## 3.3 Identification and authentication for re-key requests

### 3.3.1 Identification and authentication for routine re-key

No stipulation.

### 3.3.2 Identification and authentication for re-key after revocation

No stipulation.

## 3.4 Identification and authentication for revocation request

No stipulation.

# 4. CERTIFICATE LIFE-CYCLE OPERATIONAL REQUIREMENTS

## 4.1 Certificate application

### 4.1.1 Who can submit a certificate application

No stipulation.

### 4.1.2 Enrollment process and responsibilities

Prior to the issuance of a Certificate, the CA SHALL obtain the following documentation from the Applicant:

1. A Certificate Request; and
2. An executed Subscriber Agreement and/or Terms of Use.

The Certificate Request and Subscriber Agreement or Terms of Use MUST be in a form prescribed by the CA and MUST comply with these Requirements including [Section 9.6.3](#963-subscriber-representations-and-warranties). The CA SHOULD obtain any additional documentation the CA determines necessary to fulfil these Requirements.

The Certificate Request MUST contain a request from, or on behalf of, the Applicant for the issuance of a Certificate, and a certification by, or on behalf of, the Applicant that all of the information contained therein is correct.

One Certificate Request MAY suffice for multiple Certificates to be issued to the same Applicant, subject to the validation reuse periods described in [Section 4.2.1](#421-performing-identification-and-authentication-functions), provided that each Certificate is supported by a valid, current Certificate Request signed by the appropriate Applicant Representative on behalf of the Applicant. 

A CA may rely on a previously verified Certificate Request to issue a replacement Certificate if:

1.  The previous Certificate being referenced was not revoked;
2.  The expiration date of the replacement Certificate is the same as the previous Certificate being referenced; and
3.  The Subject Information of the Certificate is the same as the previous Certificate being referenced.

## 4.2 Certificate application processing

### 4.2.1 Performing identification and authentication functions

Applicant information SHALL include, but not be limited to, at least one `rfc822Name` or one `otherName` of type `id-on-SmtpUTF8Mailbox` to be included in the Certificate's `subjectAltName` extension.

[Section 6.3.2](#632-certificate-operational-periods-and-key-pair-usage-periods) limits the validity period of Subscriber Certificates. 

The CA MAY reuse completed validations and/or supporting evidence performed in accordance with [Section 3.2](#32-initial-identity-validation) within the following limits:

1.  **Validation of mailbox authorization or control**: Completed validation of the control of a mail server in accordance with [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain) or [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers) MUST be obtained no more than 398 days prior to issuing the Certificate. 
   
      In the event of changes to the TLS Baseline Requirements methods specified in [Section 3.2.2.1](#3221-validating-authority-over-mailbox-via-domain), a CA MAY continue to reuse completed validations and/or supporting evidence for the period stated in this section unless otherwise directed in a ballot.

      Completed validation of control of a mailbox in accordance with [Section 3.2.2.2](#3222-validating-control-over-mailbox-via-email) MUST be obtained no more than 30 days prior to issuing the Certificate.

2.  **Authentication of organization identity**: Completed validation of organization identity in accordance with [Section 3.2.3](#323-authentication-of-organization-identity) MUST be obtained no more than 398 days prior to issuing the Certificate. 
 
      Validation of authority in in accordance with [Section 3.2.6](#326-validation-of-authority) MUST be obtained no more than 398 days prior to issuing the Certificate, unless a contract between the CA and the Applicant specifies a different term. For example, the contract MAY include the perpetual assignment of roles until revoked by the Applicant or CA, or until the contract expires or is terminated.

3.  **Authentication of individual identity**: Completed validation of Individual identity in accordance with [Section 3.2.4](#324-authentication-of-individual-identity) MUST be obtained no more than 825 days prior to issuing the Certificate. 

A prior validation SHALL NOT be reused if any data or document used in the prior validation was obtained more than the maximum time permitted for reuse of the data or document prior to issuing the Certificate.

### 4.2.2 Approval or rejection of certificate applications

No stipulation.

### 4.2.3 Time to process certificate applications

No stipulation.

## 4.3 Certificate issuance


### 4.3.1 CA actions during certificate issuance

Certificate issuance by the Root CA SHALL require at least two individuals authorized by the CA (i.e. the CA system operator, system officer, or PKI administrator) one of whom deliberately issues a direct command in order for the Root CA to perform a Certificate signing operation.

### 4.3.2 Notification to subscriber by the CA of issuance of certificate

No stipulation.

## 4.4 Certificate acceptance

### 4.4.1 Conduct constituting certificate acceptance

No stipulation.

### 4.4.2 Publication of the certificate by the CA

No stipulation.

### 4.4.3 Notification of certificate issuance by the CA to other entities

No stipulation.

## 4.5 Key pair and certificate usage

### 4.5.1 Subscriber private key and certificate usage

See [Section 9.6.3](#963-subscriber-representations-and-warranties), provisions 2. and 4.

### 4.5.2 Relying party public key and certificate usage

No stipulation.

## 4.6 Certificate renewal

### 4.6.1 Circumstance for certificate renewal

No stipulation.

### 4.6.2 Who may request renewal

No stipulation.

### 4.6.3 Processing certificate renewal requests

No stipulation.

### 4.6.4 Notification of new certificate issuance to subscriber

No stipulation.

### 4.6.5 Conduct constituting acceptance of a renewal certificate

No stipulation.

### 4.6.6 Publication of the renewal certificate by the CA

No stipulation.

### 4.6.7 Notification of certificate issuance by the CA to other entities

No stipulation.

## 4.7 Certificate re-key

### 4.7.1 Circumstance for certificate re-key

No stipulation.

### 4.7.2 Who may request certification of a new public key

No stipulation.

### 4.7.3 Processing certificate re-keying requests

No stipulation.

### 4.7.4 Notification of new certificate issuance to subscriber

No stipulation.

### 4.7.5 Conduct constituting acceptance of a re-keyed certificate

No stipulation.

### 4.7.6 Publication of the re-keyed certificate by the CA

No stipulation.

### 4.7.7 Notification of certificate issuance by the CA to other entities

No stipulation.

## 4.8 Certificate modification

### 4.8.1 Circumstance for certificate modification

No stipulation.

### 4.8.2 Who may request certificate modification

No stipulation.

### 4.8.3 Processing certificate modification requests

No stipulation.

### 4.8.4 Notification of new certificate issuance to subscriber

No stipulation.

### 4.8.5 Conduct constituting acceptance of modified certificate

No stipulation.

### 4.8.6 Publication of the modified certificate by the CA

No stipulation.

### 4.8.7 Notification of certificate issuance by the CA to other entities

No stipulation.

## 4.9 Certificate revocation and suspension

### 4.9.1 Circumstances for revocation

#### 4.9.1.1 Reasons for revoking a subscriber certificate

The CA SHALL revoke a Certificate within 24 hours if one or more of the following occurs:

1. The Subscriber requests in writing that the CA revoke the Certificate;
2. The Subscriber notifies the CA that the original Certificate Request was not authorized and does not retroactively grant authorization;
3. The CA obtains evidence that the Subscriber's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise;
4. The CA is made aware of a demonstrated or proven method that can easily compute the Subscriber's Private Key based on the Public Key in the Certificate (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>);
5. The CA obtains evidence that the validation of domain authorization or mailbox control for any email address in the Certificate should not be relied upon.

The CA SHOULD revoke a Certificate within 24 hours and MUST revoke a Certificate within 5 days if one or more of the following occurs:

1. The Certificate no longer complies with the requirements of [Section 6.1.5](#615-key-sizes) and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
2. The CA obtains evidence that the Certificate was misused;
3. The CA is made aware that a Subscriber has violated one or more of its material obligations under the Subscriber Agreement or Terms of Use;
4. The CA is made aware of any circumstance indicating that use of an email address or Fully-Qualified Domain Name in the Certificate is no longer legally permitted (e.g. a court or arbitrator has revoked the right to use an email address or Domain Name, a relevant licensing or services agreement between the Subscriber has terminated, or the account holder has failed to maintain the active status of the email address or Domain Name);
5. The CA is made aware of a material change in the information contained in the Certificate;
6. The CA is made aware that the Certificate was not issued in accordance with these Requirements or the CA's CP and/or CPS;
7. The CA determines or is made aware that any of the information appearing in the Certificate is inaccurate;
8. The CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the CA has made arrangements to continue maintaining the CRL/OCSP Repository;
9.  Revocation is required by the CA's CP and/or CPS; or
10. The CA is made aware of a demonstrated or proven method that exposes the Subscriber's Private Key to compromise or if there is clear evidence that the specific method used to generate the Private Key was flawed.

#### 4.9.1.2 Reasons for revoking a subordinate CA certificate

The Issuing CA SHALL revoke a Subordinate CA Certificate within seven (7) days if one or more of the following occurs:

1. The Subordinate CA requests revocation in writing;
2. The Subordinate CA notifies the Issuing CA that the original Certificate Request was not authorized and does not retroactively grant authorization;
3. The Issuing CA obtains evidence that the Subordinate CA's Private Key corresponding to the Public Key in the Certificate suffered a Key Compromise or no longer complies with the requirements of [Section 6.1.5](#615-key-sizes) and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
4. The Issuing CA obtains evidence that the Certificate was misused;
5. The Issuing CA is made aware that the Certificate was not issued in accordance with or that Subordinate CA has not complied with this document or the applicable CP and/or CPS;
6. The Issuing CA determines that any of the information appearing in the Certificate is inaccurate or misleading;
7. The Issuing CA or Subordinate CA ceases operations for any reason and has not made arrangements for another CA to provide revocation support for the Certificate;
8. The Issuing CA's or Subordinate CA's right to issue Certificates under these Requirements expires or is revoked or terminated, unless the Issuing CA has made arrangements to continue maintaining the CRL/OCSP Repository; or
9. Revocation is required by the Issuing CA's CP and/or CPS.

### 4.9.2 Who can request revocation

The Subscriber, RA, or Issuing CA can initiate revocation. Additionally, Subscribers, Relying Parties, Application Software Suppliers, and other third parties MAY submit Certificate Problem Reports informing the Issuing CA of reasonable cause to revoke a Certificate.

### 4.9.3 Procedure for revocation request

The CA SHALL provide a process for Subscribers to request revocation of their own Certificates. The process MUST be described in the CA's CP and/or CPS. The CA SHALL maintain a continuous 24x7 ability to accept and respond to revocation requests and Certificate Problem Reports.

The CA SHALL provide clear instructions for reporting suspected Private Key Compromise, Certificate misuse, or other types of fraud, compromise, misuse, inappropriate conduct, or any other matter related to Certificates. The CA SHALL publicly disclose the instructions through a readily accessible online means and in Section 1.5.2 of their CPS.

### 4.9.4 Revocation request grace period

No stipulation.

### 4.9.5 Time within which CA must process the revocation request

Within 24 hours after receiving a Certificate Problem Report, the CA SHALL investigate the facts and circumstances related to a Certificate Problem Report and provide a preliminary report on its findings to both the Subscriber and the entity who filed the Certificate Problem Report.

After reviewing the facts and circumstances, the CA SHALL work with the Subscriber and any entity reporting the Certificate Problem Report or other revocation-related notice to establish whether or not the Certificate will be revoked, and if so, a date on which the CA will revoke the Certificate. The period from receipt of the Certificate Problem Report or revocation-related notice to published revocation MUST NOT exceed the time frame set forth in [Section 4.9.1.1](#4911-reasons-for-revoking-a-subscriber-certificate). The date selected by the CA SHOULD consider the following criteria:

1. The nature of the alleged problem (scope, context, severity, magnitude, risk of harm);
2. The consequences of revocation (direct and collateral impacts to Subscribers and Relying Parties);
3. The number of Certificate Problem Reports received about a particular Certificate or Subscriber;
4. The entity making the complaint (for example, a complaint from a law enforcement official that a Web site is engaged in illegal activities should carry more weight than a complaint from a consumer alleging that they didn't receive the goods they ordered); and
5. Relevant legislation.
   
### 4.9.6 Revocation checking requirement for relying parties

No stipulation.

**Note**: Following Certificate issuance, a Certificate may be revoked for reasons stated in [Section 4.9](#49-certificate-revocation-and-suspension). Therefore, Relying Parties SHOULD check the revocation status of all Certificates that contain a CDP or OCSP pointer.

### 4.9.7 CRL issuance frequency

For the status of Subscriber Certificates: if the CA publishes a CRL, then the CA SHALL update and reissue CRLs at least once every seven days, and the value of the `nextUpdate` field MUST NOT be more than ten days beyond the value of the `thisUpdate` field.

For the status of Subordinate CA Certificates: the CA SHALL update and reissue CRLs at least:

1. once every twelve months; and
2. within 24 hours after revoking a Subordinate CA Certificate.

The value of the `nextUpdate` field MUST NOT be more than twelve months beyond the value of the `thisUpdate` field.

### 4.9.8 Maximum latency for CRLs

No stipulation.

### 4.9.9 On-line revocation/status checking availability

OCSP responses MUST conform to [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960) and/or [RFC 5019](https://datatracker.ietf.org/doc/html/rfc5019). OCSP responses MUST either:

1. Be signed by the CA that issued the Certificates whose revocation status is being checked, or
2. Be signed by an OCSP Responder whose Certificate is signed by the CA that issued the Certificate whose revocation status is being checked.
   
In the latter case, the OCSP signing Certificate MUST contain the ocspSigning EKU (1.3.6.1.5.5.7.3.9) and an extension of type `id-pkix-ocsp-nocheck`, as defined by [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960).

### 4.9.10 On-line revocation checking requirements

OCSP responders operated by the CA SHALL support the HTTP GET method, as described in [RFC 6960](https://datatracker.ietf.org/doc/html/rfc6960) and/or [RFC 5019](https://datatracker.ietf.org/doc/html/rfc5019).

The validity interval of an OCSP response is the difference in time between the thisUpdate and nextUpdate field, inclusive. For purposes of computing differences, a difference of 3,600 seconds SHALL be equal to one hour, and a difference of 86,400 seconds SHALL be equal to one day, ignoring leap-seconds.

For the status of Subscriber Certificates:

1. OCSP responses MUST have a validity interval greater than or equal to eight hours;
2. OCSP responses MUST have a validity interval less than or equal to ten days;
3. For OCSP responses with validity intervals less than sixteen hours, then the CA SHALL update the information provided via an Online Certificate Status Protocol prior to one-half of the validity period before the nextUpdate; and
4. For OCSP responses with validity intervals greater than or equal to sixteen hours, then the CA SHALL update the information provided via an Online Certificate Status Protocol at least eight hours prior to the nextUpdate, and no later than four days after the thisUpdate.
   
For the status of Subordinate CA Certificates, the CA SHALL update information provided via OCSP:

1. at least every twelve months; and
2. within 24 hours after revoking a Subordinate CA Certificate.

If the OCSP responder receives a request for the status of a Certificate serial number that is "unused", then the responder SHOULD NOT respond with a "good" status. If the OCSP responder is for a CA that is not Technically Constrained in line with [Section 7.1.5](#715-name-constraints), the responder MUST NOT respond with a "good" status for such requests.

The CA SHOULD monitor the OCSP responder for requests for "unused" serial numbers as part of its security response procedures.

A Certificate serial number within an OCSP request is "assigned" if a Certificate with that serial number has been issued by the Issuing CA, using any current or previous key associated with that CA subject, or "unused" if otherwise.

### 4.9.11 Other forms of revocation advertisements available

No stipulation.

### 4.9.12 Special requirements re key compromise

See [Section 4.9.1](#491-circumstances-for-revocation).

### 4.9.13 Circumstances for suspension

The Repository MUST NOT include entries that indicate that a Certificate is suspended.

### 4.9.14 Who can request suspension

No stipulation.

### 4.9.15 Procedure for suspension request

No stipulation.

### 4.9.16 Limits on suspension period

No stipulation.

## 4.10 Certificate status services

### 4.10.1 Operational characteristics

Revocation entries on a CRL or OCSP Response MUST NOT be removed until after the Expiry Date of the revoked Certificate.

### 4.10.2 Service availability

The CA SHALL operate and maintain its CRL and OCSP capability with resources sufficient to provide a response time of ten seconds or less under normal operating conditions.

The CA SHALL maintain an online 24x7 Repository that application software can use to automatically check the current status of all unexpired Certificates issued by the CA.

The CA SHALL maintain a continuous 24x7 ability to respond internally to a high-priority Certificate Problem Report, and where appropriate, forward such a complaint to law enforcement authorities, and/or revoke a Certificate that is the subject of such a complaint.

### 4.10.3 Optional features

No stipulation.

## 4.11 End of subscription

No stipulation.

## 4.12 Key escrow and recovery

### 4.12.1 Key escrow and recovery policy and practices

No stipulation.

### 4.12.2 Session key encapsulation and recovery policy and practices

No stipulation.

# 5. FACILITY, MANAGEMENT, AND OPERATIONAL CONTROLS

The CA/Browser Forum's Network and Certificate System Security Requirements are incorporated by reference as if fully set forth herein.

The CA SHALL develop, implement, and maintain a comprehensive security program designed to:

1. Protect the confidentiality, integrity, and availability of Certificate Data and Certificate Management Processes;
2. Protect against anticipated threats or hazards to the confidentiality, integrity, and availability of the Certificate Data and Certificate Management Processes;
3. Protect against unauthorized or unlawful access, use, disclosure, alteration, or destruction of any Certificate Data or Certificate Management Processes;
4. Protect against accidental loss or destruction of, or damage to, any Certificate Data or Certificate Management Processes; and
5. Comply with all other security requirements applicable to the CA by law.

The Certificate Management Process MUST include:

1. physical security and environmental controls;
2. system integrity controls, including configuration management, integrity maintenance of trusted code, and malware detection/prevention;
3. network security and firewall management, including port restrictions and IP address filtering;
4. user management, separate trusted-role assignments, education, awareness, and training; and
5. logical access controls, activity logging, and inactivity time-outs to provide individual accountability.

The CA's security program MUST include an annual Risk Assessment that:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;
2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and
3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

Based on the Risk Assessment, the CA SHALL develop, implement, and maintain a security plan consisting of security procedures, measures, and products designed to achieve the objectives set forth above and to manage and control the risks identified during the Risk Assessment, commensurate with the sensitivity of the Certificate Data and Certificate Management Processes. The security plan MUST include administrative, organizational, technical, and physical safeguards appropriate to the sensitivity of the Certificate Data and Certificate Management Processes. The security plan MUST also take into account then-available technology and the cost of implementing the specific measures, and SHALL implement a reasonable level of security appropriate to the harm that might result from a breach of security and the nature of the data to be protected.

## 5.1 Physical controls

### 5.1.1 Site location and construction

### 5.1.2 Physical access

No stipulation.

### 5.1.3 Power and air conditioning

No stipulation.

### 5.1.4 Water exposures

No stipulation.

### 5.1.5 Fire prevention and protection

No stipulation.

### 5.1.6 Media storage

No stipulation.

### 5.1.7 Waste disposal

No stipulation.

### 5.1.8 Off-site backup

No stipulation.

## 5.2 Procedural controls

### 5.2.1 Trusted roles

No stipulation.

### 5.2.2 Number of persons required per task

CA Private Keys SHALL be backed up, stored, and recovered only by personnel in trusted roles using, at least, dual control in a physically secured environment.

### 5.2.3 Identification and authentication for each role

No stipulation.

### 5.2.4 Roles requiring separation of duties

No stipulation.

## 5.3 Personnel controls

### 5.3.1 Qualifications, experience, and clearance requirements

Prior to the engagement of any person in the Certificate Management Process, whether as an employee, agent, or an independent contractor of the CA, the CA SHALL verify the identity and trustworthiness of such person.

### 5.3.2 Background check procedures

No stipulation.

### 5.3.3 Training requirements

The CA SHALL provide all personnel performing information verification duties with skills-training that covers basic Public Key Infrastructure knowledge, authentication and vetting policies and procedures (including the CA's CP and/or CPS), common threats to the information verification process (including phishing and other social engineering tactics), and these Requirements.

The CA SHALL maintain records of such training and ensure that personnel entrusted with Validation Specialist duties maintain a skill level that enables them to perform such duties satisfactorily.

The CA SHALL document that each Validation Specialist possesses the skills required by a task before allowing the Validation Specialist to perform that task.

The CA SHALL require all Validation Specialists to pass an examination provided by the CA on the information verification requirements outlined in these Requirements.

### 5.3.4 Retraining frequency and requirements

All personnel in Trusted roles SHALL maintain skill levels consistent with the CA's training and performance programs.

### 5.3.5 Job rotation frequency and sequence

No stipulation.

### 5.3.6 Sanctions for unauthorized actions

No stipulation.

### 5.3.7 Independent contractor requirements

The CA SHALL verify that the Delegated Third Party's personnel involved in the issuance of a Certificate meet the training and skills requirements of [Section 5.3.3](#533--training-requirements) and the document retention and event logging requirements of [Section 5.4.1](#541-types-of-events-recorded).

### 5.3.8 Documentation supplied to personnel

No stipulation.

## 5.4 Audit logging procedures

### 5.4.1 Types of events recorded

The CA and each Delegated Third Party SHALL record events related to the security of their Certificate Systems, Certificate Management Systems, Root CA Systems, and Delegated Third Party Systems. The CA and each Delegated Third Party SHALL record events related to their actions taken to process a certificate request and to issue a Certificate, including all information generated and documentation received in connection with the certificate request; the time and date; and the personnel involved. The CA SHALL make these records available to its Qualified Auditor as proof of the CA’s compliance with these Requirements.

The CA SHALL record at least the following events:

1. CA Certificate and key lifecycle events, including:
   1. Key generation, backup, storage, recovery, archival, and destruction;
   2. Certificate requests, renewal, and re-key requests, and revocation;
   3. Approval and rejection of Certificate Requests;
   4. Cryptographic device lifecycle management events;
   5. Generation of Certificate Revocation Lists;
   6. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)); and
   7. Introduction of new Certificate Profiles and retirement of existing Certificate Profiles.

2. Subscriber Certificate lifecycle management events, including:
   1. Certificate requests, renewal, and re-key requests, and revocation;
   2. All verification activities stipulated in these Requirements and the CA's Certification Practice Statement;
   3. Approval and rejection of certificate requests;
   4. Issuance of Certificates;
   5. Generation of Certificate Revocation Lists; and
   6. Signing of OCSP Responses (as described in [Section 4.9](#49-certificate-revocation-and-suspension) and [Section 4.10](#410-certificate-status-services)).

3. Security events, including:
   1. Successful and unsuccessful PKI system access attempts;
   2. PKI and security system actions performed;
   3. Security profile changes;
   4. Installation, update and removal of software on a Certificate System;
   5. System crashes, hardware failures, and other anomalies;
   6. Firewall and router activities; and
   7. Entries to and exits from the CA facility.

Log records MUST include the following elements:

1. Date and time of event;
2. Identity of the person making the journal record; and
3. Description of the event.

### 5.4.2 Frequency of processing audit log

No stipulation.

### 5.4.3 Retention period for audit log

The CA and each Delegated Third Party SHALL retain, for at least two (2) years:

  1. CA Certificate and key lifecycle management event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (1)) after the later occurrence of:
     1. the destruction of the CA Private Key; or
     2. the revocation or expiration of the final CA Certificate in that set of Certificates that have an X.509v3 `basicConstraints` extension with the `cA` field set to true and which share a common Public Key corresponding to the CA Private Key;
  2. Subscriber Certificate lifecycle management event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (2)) after the expiration of the Subscriber Certificate;
  3. Any security event records (as set forth in [Section 5.4.1](#541-types-of-events-recorded) (3)) after the event occurred.

Note: While these Requirements set the minimum retention period, the CA MAY choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past audit log events.

### 5.4.4 Protection of audit log

No stipulation.

### 5.4.5 Audit log backup procedures

No stipulation.

### 5.4.6 Audit collection System (internal vs. external)

No stipulation.

### 5.4.7 Notification to event-causing subject

No stipulation.

### 5.4.8 Vulnerability assessments

The CA's security program MUST include an annual Risk Assessment that:

1. Identifies foreseeable internal and external threats that could result in unauthorized access, disclosure, misuse, alteration, or destruction of any Certificate Data or Certificate Management Processes;
2. Assesses the likelihood and potential damage of these threats, taking into consideration the sensitivity of the Certificate Data and Certificate Management Processes; and
3. Assesses the sufficiency of the policies, procedures, information systems, technology, and other arrangements that the CA has in place to counter such threats.

## 5.5 Records archival

### 5.5.1 Types of records archived

The CA and each Delegated Party SHALL archive all audit logs (as set forth in [Section 5.4.1](#541-types-of-events-recorded)).

Additionally, the CA and each Delegated Party SHALL archive:
1. Documentation related to the security of their Certificate Systems, Certificate Management Systems, Root CA Systems, and Delegated Third Party Systems; and
2. Documentation related to their verification, issuance, and revocation of certificate requests and Certificates.

### 5.5.2 Retention period for archive

Archived audit logs (as set forth in [Section 5.5.1](#551-types-of-records-archived) SHALL be retained for a period of at least two (2) years from their record creation timestamp, or as long as they are required to be retained per [Section 5.4.3](#543-retention-period-for-audit-log), whichever is longer.

Additionally, the CA and each delegated party SHALL retain, for at least two (2) years:
1. All archived documentation related to the security of Certificate Systems, Certificate Management Systems, Root CA Systems and Delegated Third Party Systems (as set forth in [Section 5.5.1](#551-types-of-records-archived)); and
2. All archived documentation relating to the verification, issuance, and revocation of certificate requests and Certificates (as set forth in [Section 5.5.1](#551-types-of-records-archived)) after the later occurrence of:
   1. such records and documentation were last relied upon in the verification, issuance, or revocation of certificate requests and Certificates; or
   2. the expiration of the Subscriber Certificates relying upon such records and documentation.

Note: While these Requirements set the minimum retention period, the CA MAY choose a greater value as more appropriate in order to be able to investigate possible security or other types of incidents that will require retrospection and examination of past records archived.

### 5.5.3 Protection of archive

No stipulation.

### 5.5.4 Archive backup procedures

No stipulation.

### 5.5.5 Requirements for time-stamping of records

No stipulation.

### 5.5.6 Archive collection system (internal or external)

No stipulation.

### 5.5.7 Procedures to obtain and verify archive information

No stipulation.

## 5.6 Key changeover

No stipulation.

## 5.7 Compromise and disaster recovery

### 5.7.1 Incident and compromise handling procedures

CA operators SHALL have an Incident Response Plan and a Disaster Recovery Plan.

The CA SHALL document a business continuity and disaster recovery procedures designed to notify and reasonably protect Application Software Suppliers, Subscribers, and Relying Parties in the event of a disaster, security compromise, or business failure. The CA is not required to publicly disclose its business continuity plans but SHALL make its business continuity plan and security plans available to the CA's auditors upon request. The CA SHALL annually test, review, and update these procedures.

The business continuity plan MUST include:

1. The conditions for activating the plan;
2. Emergency procedures;
3. Fallback procedures;
4. Resumption procedures;
5. A maintenance schedule for the plan;
6. Awareness and education requirements;
7. The responsibilities of the individuals;
8. Recovery time objective (RTO);
9. Regular testing of contingency plans;
10. The CA's plan to maintain or restore the CA's business operations in a timely manner following interruption to or failure of critical business processes;
11. A requirement to store critical cryptographic materials (i.e., secure cryptographic device and activation materials) at an alternate location;
12. What constitutes an acceptable system outage and recovery time;
13. How frequently backup copies of essential business information and software are taken;
14. The distance of recovery facilities to the CA's main site; and
15. Procedures for securing its facility to the extent possible during the period of time following a disaster and prior to restoring a secure environment either at the original or a remote site.

### 5.7.2 Computing resources, software, and/or data are corrupted

No stipulation.

### 5.7.3 Entity private key compromise procedures

No stipulation.

### 5.7.4 Business continuity capabilities after a disaster

No stipulation.

## 5.8 CA or RA termination

No stipulation.

# 6. TECHNICAL SECURITY CONTROLS

## 6.1 Key pair generation and installation

### 6.1.1 Key pair generation

#### 6.1.1.1 CA key pair generation

For CA Key Pairs that are either

  1. used as a CA Key Pair for a Root CA Certificate; or
  2. used as a CA Key Pair for a Subordinate CA Certificate, where the Subordinate CA is not the operator of the Root CA or an Affiliate of the Root CA,

the CA SHALL:

1. prepare and follow a Key Generation Script;
2. have a Qualified Auditor witness the CA Key Pair generation process or record a video of the entire CA Key Pair generation process; and
3. have a Qualified Auditor issue a report opining that the CA followed its key ceremony during its Key and Certificate generation process and the controls used to ensure the integrity and confidentiality of the Key Pair.

For other CA Key Pairs that are for the operator of the Root CA or an Affiliate of the Root CA, the CA SHOULD:

1. prepare and follow a Key Generation Script; and
2. either (i) have a Qualified Auditor witness the CA Key Pair generation process, or (ii) video-record the entire CA Key Pair generation process for review by its Qualified Auditor.

In all cases, the CA SHALL:

1. generate the CA Key Pair in a physically secured environment as described in the CA's CP and/or CPS;
2. generate the CA Key Pair using personnel in Trusted Roles under the principles of multiple person control and split knowledge;
3. generate the CA Key Pair within cryptographic modules meeting the applicable technical and business requirements as disclosed in the CA's CP and/or CPS;
4. log its CA Key Pair generation activities; and
5. maintain effective controls to provide reasonable assurance that the Private Key was generated and protected in conformance with the procedures described in its CP and/or CPS and (if applicable) its Key Generation Script.

#### 6.1.1.2 RA key pair generation

No stipulation.

#### 6.1.1.3 Subscriber key pair generation

The CA SHALL reject a Certificate Request if one or more of the following conditions are met:

1. The Key Pair does not meet the requirements set forth in [Section 6.1.5](#615-key-sizes) and/or [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking);
2. There is clear evidence that the specific method used to generate the Private Key was flawed;
3. The CA is aware of a demonstrated or proven method that exposes the Applicant's Private Key to compromise;
4. The CA has previously been made aware that the Applicant's Private Key has suffered a Key Compromise, such as through the provisions of [Section 4.9.1.1](#4911-reasons-for-revoking-a-subscriber-certificate);
5. The CA is aware of a demonstrated or proven method to easily compute the Applicant's Private Key based on the Public Key (such as a Debian weak key, see <https://wiki.debian.org/SSLkeys>).

### 6.1.2 Private key delivery to subscriber

Parties other than the Subscriber SHALL NOT archive the Subscriber Private Key without authorization by the Subscriber.

If the CA or any of its designated RAs become aware that a Subscriber's Private Key has been communicated to a person or organization not authorized by the Subscriber, then the CA SHALL revoke all Certificates that include the Public Key corresponding to the communicated Private Key.

### 6.1.3 Public key delivery to certificate issuer

No stipulation.

### 6.1.4 CA public key delivery to relying parties

No stipulation.

### 6.1.5 Key sizes

For RSA key pairs the CA SHALL:

* Ensure that the modulus size, when encoded, is at least 2048 bits, and;
* Ensure that the modulus size, in bits, is evenly divisible by 8.

For ECDSA key pairs, the CA SHALL:

* Ensure that the key represents a valid point on the NIST P-256, NIST P-384 or NIST P-521 elliptic curve.

For EdDSA key pairs, the CA SHALL:

* Ensure that the key represents a valid point on the curve25519 or curve 448 elliptic curve.
  
No other algorithms or key sizes are permitted.

### 6.1.6 Public key parameters generation and quality checking

For RSA key pairs: the CA SHALL confirm that the value of the public exponent is an odd number equal to 3 or more. Additionally, the public exponent SHOULD be in the range between 2^16 + 1 and 2^256 - 1. The modulus SHOULD also have the following characteristics: an odd number, not the power of a prime, and have no factors smaller than 752. [Source: Section 5.3.3, NIST SP 800-89]

For ECDSA key pairs: the CA SHOULD confirm the validity of all keys using either the ECC Full Public Key Validation Routine or the ECC Partial Public Key Validation Routine. [Source: Sections 5.6.2.3.2 and 5.6.2.3.3, respectively, of NIST SP 800-56A: Revision 2]

### 6.1.7 Key usage purposes (as per X.509 v3 key usage field)

Private Keys corresponding to Root CA Certificates MUST NOT be used to sign Certificates except in the following cases:

1. Self-signed Certificates to represent the Root CA itself;
2. Certificates for Subordinate CAs and Cross Certificates;
3. Certificates for infrastructure purposes (administrative role certificates, internal CA operational device certificates); and
4. Certificates for OCSP Response verification.

## 6.2 Private key protection and cryptographic module engineering controls

The CA SHALL implement physical and logical safeguards to prevent unauthorized Certificate issuance. Protection of the CA Private Key outside the validated system or device specified above MUST consist of physical security, encryption, or a combination of both, implemented in a manner that prevents disclosure of the Private Key. The CA SHALL encrypt its Private Key with an algorithm and key-length that, according to the state of the art, are capable of withstanding cryptanalytic attacks for the residual life of the encrypted key or key part.

### 6.2.1 Cryptographic module standards and controls

No stipulation.

### 6.2.2 Private key (n out of m) multi-person control

No stipulation.

### 6.2.3 Private key escrow

No stipulation.

### 6.2.4 Private key backup

See [Section 5.2.2](#522-number-of-persons-required-per-task).

### 6.2.5 Private key archival

Parties other than the Subordinate CA SHALL NOT archive the Subordinate CA Private Keys without authorization by the Subordinate CA.

### 6.2.6 Private key transfer into or from a cryptographic module

If the Issuing CA generated the Private Key on behalf of the Subordinate CA, then the Issuing CA SHALL encrypt the Private Key for transport to the Subordinate CA. If the Issuing CA becomes aware that a Subordinate CA's Private Key has been communicated to an unauthorized person or an organization not Affiliated with the Subordinate CA, then the Issuing CA SHALL revoke all certificates that include the Public Key corresponding to the communicated Private Key.

### 6.2.7 Private key storage on cryptographic module

The CA SHALL protect its Private Key in a system or device that has been validated as meeting at least FIPS 140 level 3 or an appropriate Common Criteria Protection Profile or Security Target, EAL 4 (or higher), which includes requirements to protect the Private Key and other assets against known threats.

### 6.2.8 Method of activating private key

No stipulation.

### 6.2.9 Method of deactivating private key

No stipulation.

### 6.2.10 Method of destroying private key

No stipulation.

### 6.2.11 Cryptographic module rating

No stipulation.

## 6.3 Other aspects of key pair management

### 6.3.1 Public key archival

No stipulation.

### 6.3.2 Certificate operational periods and key pair usage periods

| Generation | Maximum Validity Period      | 
|------|-----------------------|
| Strict and Multipurpose | 825 days |
| Legacy | 1185 days |

For the purpose of calculations, a day is measured as 86,400 seconds. Any amount of time greater than this, including fractional seconds and/or leap seconds, SHALL represent an additional day. For this reason, Subscriber Certificates SHOULD NOT be issued for the maximum permissible time by default, in order to account for such adjustments.

## 6.4 Activation data

### 6.4.1 Activation data generation and installation

No stipulation.

### 6.4.2 Activation data protection

No stipulation.

### 6.4.3 Other aspects of activation data

No stipulation.

## 6.5 Computer security controls

### 6.5.1 Specific computer security technical requirements

The CA SHALL enforce multi-factor authentication for all accounts capable of directly causing certificate issuance.

### 6.5.2 Computer security rating

No stipulation.

## 6.6 Life cycle technical controls

### 6.6.1 System development controls

No stipulation.

### 6.6.2 Security management controls

No stipulation.

### 6.6.3 Life cycle security controls

No stipulation.

## 6.7 Network security controls

No stipulation.

## 6.8 Time-stamping

No stipulation.

# 7. CERTIFICATE, CRL, AND OCSP PROFILES

## 7.1 Certificate profile

The CA SHALL meet the technical requirements set forth in [Section 2.2](#22--publication-of-certification-information), [Section 6.1.5](#615-key-sizes), and [Section 6.1.6](#616-public-key-parameters-generation-and-quality-checking).

CAs SHALL generate non-sequential Certificate serial numbers greater than zero (0) and less than 2^159 containing at least 64 bits of output from a CSPRNG.

### 7.1.1 Version number(s)

Certificates MUST be of type X.509 v3.

### 7.1.2 Certificate content and extensions; application of RFC 6818

This section specifies the additional requirements for Certificate content and extensions for Certificates.

#### 7.1.2.1 Root CA certificates

a. `basicConstraints` (MUST be present)

   This extension MUST be marked critical. The `cA` field MUST be set true. The `pathLenConstraint` field SHOULD NOT be present.

b. `keyUsage` (MUST be present)

   This extension MUST be marked critical. Bit positions for `keyCertSign` and `cRLSign` MUST be set. If the Root CA Private Key is used for signing OCSP responses, then the `digitalSignature` bit MUST be set.

c. `certificatePolicies` (SHOULD NOT be present)

   This extension SHOULD NOT be present.

d. `extKeyUsage` (MUST NOT be present)

   This extension MUST NOT be present.

#### 7.1.2.2 Subordinate CA certificates

a. `certificatePolicies` (MUST be present)

   This extension SHOULD NOT be marked critical.

   If the value of this extension includes a `PolicyInformation` which contains a qualifier of type `id-qt-cps` (OID: 1.3.6.1.5.5.7.2.1), then the value of the qualifier MUST be a HTTP or HTTPS URL for the Issuing CA's CP and/or CPS, Relying Party Agreement, or other pointer to online policy information provided by the Issuing CA.  If a qualifier of type `id-qt-unotice` (OID: 1.3.6.1.5.5.7.2.2) is included, then it MUST contain `explicitText` and MUST NOT contain `noticeRef`. 

b. `cRLDistributionPoints` (MUST be present)

   This extension MUST be present and MUST NOT be marked critical. It MUST contain the HTTP URL of the CA's CRL service.

c. `authorityInformationAccess` (SHOULD be present)

   This extension MUST NOT be marked critical.

   It SHOULD contain the HTTP URL of the Issuing CA Certificate (`accessMethod` = 1.3.6.1.5.5.7.48.2).
   It MAY contain the HTTP URL of the Issuing CA OCSP responder (`accessMethod` = 1.3.6.1.5.5.7.48.1).

d. `basicConstraints` (MUST be present)

   This extension MUST be marked critical. The `cA` field MUST be set true. The `pathLenConstraint` field MAY be present.

e. `keyUsage` (MUST be present)

   This extension MUST be marked critical. Bit positions for `keyCertSign` and `cRLSign` MUST be set. If the Subordinate CA Private Key is used for signing OCSP responses, then the `digitalSignature` bit MUST be set.

f. `nameConstraints` (MAY be present)

   This extension SHOULD be marked critical[^*].

[^*]: Non-critical Name Constraints are an exception to [RFC 5280 (4.2.1.10)](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.10), however, they MAY be used until the `nameConstraints` extension is supported by Application Software Suppliers whose software is used by a substantial portion of Relying Parties worldwide.

g. `extKeyUsage` (MAY be present for Cross Certificates; MUST be present otherwise)

   For Cross Certificates that share a Subject Distinguished Name and Subject Public Key with a Root CA Certificate operated in accordance with these Requirements, this extension MAY be present. If present, this extension SHOULD NOT be marked critical. This extension MUST only contain usages for which the Issuing CA has verified the Cross Certificate is authorized to assert. This extension MUST NOT contain the `anyExtendedKeyUsage` usage.

   For all other Subordinate CA Certificates, including Technically Constrained Subordinate CA Certificates:

   This extension MUST be present and SHOULD NOT be marked critical[^**].

   For Subordinate CA Certificates that will be used to issue S/MIME Certificates, the value `id-kp-emailProtection` MUST be present. The values `id-kp-serverAuth`, `id-kp-codeSigning`, `id-kp-timeStamping`, and `anyExtendedKeyUsage` MUST NOT be present. Other values MAY be present.

[^**]: While [RFC 5280, Section 4.2.1.12](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12), notes that this extension will generally only appear within end-entity Certificates, these Requirements make use of this extension to further protect relying parties by limiting the scope of Subordinate Certificates, as implemented by a number of Application Software Suppliers.

h. `authorityKeyIdentifier` (MUST be present)

   This extension MUST be present and MUST NOT be marked critical. It MUST contain a `keyIdentifier` field and it MUST NOT contain a `authorityCertIssuer` or `authorityCertSerialNumber` field.

#### 7.1.2.3 Subscriber certificates

a. `certificatePolicies` (MUST be present)

   This extension MUST be present and SHOULD NOT be marked critical. It MUST include only one of the reserved `policyIdentifiers` listed in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers), and MAY contain one or more identifiers documented by the CA in its CP and/or CPS. 

   If the value of this extension includes a `PolicyInformation` which contains a qualifier of type `id-qt-cps` (OID: 1.3.6.1.5.5.7.2.1), then the value of the qualifier MUST be a HTTP or HTTPS URL for the Issuing CA's CP and/or CPS, Relying Party Agreement, or other pointer to online policy information provided by the Issuing CA.  If a qualifier of type `id-qt-unotice` (OID: 1.3.6.1.5.5.7.2.2) is included, then it MUST contain `explicitText` and MUST NOT contain `noticeRef`. 

b. `cRLDistributionPoints` (MUST be present)

   This extension MUST be present and SHOULD NOT be marked critical. It SHALL contain at least one `distributionPoint` whose `fullName` value includes a GeneralName of type `uniformResourceIdentifier` that includes a HTTP URI where the Issuing CA's CRL can be retrieved. 
   
   For Legacy profiles only, following additional publicly accessible `fullName` LDAP, FTP, or HTTP URIs MAY be specified.

c. `authorityInformationAccess` (MUST be present)

   This extension MUST be present. It MUST NOT be marked critical, and it MUST contain at least one `accessMethod` value of type `id-ad-ocsp` that specifies the HTTP URI of the Issuing CA's OCSP responder. Additional `id-ad-ocsp` LDAP, FTP, or HTTP URIs MAY be specified. It SHOULD contain at least one `accessMethod` value of type `id-ad-caIssuers` that specifies the HTTP URI of the Issuing CA's Certificate. Additional `id-ad-caIssuers` LDAP, FTP, or HTTP URIs MAY be specified.

d. `basicConstraints` (optional)

   The `cA` field MUST NOT be true. `pathLenConstraint` field SHALL NOT be present.

e. `keyUsage` (MUST be present)

   This extension MUST be present and SHOULD be marked critical. 

   | Generation | `rsaEncryption`       | `id-ecPublicKey`            |
   |------|-----------------------|-----------------------------|
   | Strict | For signing only, bit positions MUST be set for `digitalSignature` and MAY be set for `nonRepudiation`.<br>For key management only, bit positions MUST be set for `keyEncipherment`.<br>For dual use, bit positions MUST be set for `digitalSignature` and `keyEncipherment` and MAY be set for `nonRepudiation`. |For signing only, bit positions MUST be set for `digitalSignature` and MAY be set for `nonRepudiation`.<br>For key management only, bit positions MUST be set for `keyAgreement` and MAY be set for `encipherOnly` or `decipherOnly`.<br>For dual use, bit positions MUST be set for `digitalSignature` and `keyAgreement` and MAY be set for `nonRepudiation` and for `encipherOnly` or `decipherOnly` (only if `keyAgreement` is set).|
   | Multipurpose<br> and Legacy | For signing only, bit positions MUST be set for `digitalSignature` and MAY be set for `nonRepudiation`.<br>For key management only, bit positions MUST be set for `keyEncipherment` and MAY be set for `dataEncipherment`.<br>For dual use, bit positions MUST be set for `digitalSignature` and `keyEncipherment` and MAY be set for `nonRepudiation` and `dataEncipherment`. |For signing only, bit positions MUST be set for `digitalSignature` and MAY be set for `nonRepudiation`.<br>For key management only, bit positions MUST be set for `keyAgreement` and MAY be set for `encipherOnly` or `decipherOnly`.<br>For dual use, bit positions MUST be set for `digitalSignature` and `keyAgreement` and MAY be set for `nonRepudiation` and for `encipherOnly` or `decipherOnly` (only if `keyAgreement` is set).|

   Other bit positions MUST NOT be set.

f. `extKeyUsage` (MUST be present)

   | Generation | `KeyPurposeId`      | 
   |------|-----------------------|
   | Strict | `id-kp-emailProtection` MUST be present. Other values MUST NOT be present. |
  | Multipurpose and Legacy |`id-kp-emailProtection` MUST be present. Other values MAY be present. |

   The value `anyExtendedKeyUsage` MUST NOT be present.

g. `authorityKeyIdentifier` (MUST be present)

   This extension MUST be present and MUST NOT be marked critical. The `keyIdentifier` field SHALL be present. `authorityCertIssuer` and `authorityCertSerialNumber` fields SHALL NOT be present.

h. `subjectAlternativeName` (MUST be present)

   This extension MUST be present and SHOULD NOT be marked critical unless the Subject is an empty sequence. 

   | Generation | `subjectAlternativeName`      | 
   |------|-----------------------|
   | Strict | All email addresses in Subject MUST be repeated in SAN.  MUST contain at least one item of type `rfc822Name` or `otherName` of type `id-on-SmtpUTF8Mailbox`. MUST NOT contain items of type: `dNSName`, `iPAddress`, `otherName` values other than type `id-on-SmtpUTF8Mailbox`, or `uniformResourceIdentifier`.|
   | Multipurpose and Legacy |All email addresses in Subject MUST be repeated in SAN.  MUST contain at least one item of type `rfc822Name` or `otherName` of type `id-on-SmtpUTF8Mailbox`. MUST NOT contain items of type: `dNSName`, `iPAddress`, or `uniformResourceIdentifier`.<br>`otherName` values MAY be included. `otherName` values of any other type MUST be validated in accordance with the CA's CPS. |

   `otherName` values of type `id-on-SmtpUTF8Mailbox` MUST be validated in accordance with RFC 8398.

i. `smimeCapabilities` (optional)

   This extension MAY be present and MUST NOT be marked critical. May indicate cryptographic capabilities of the sender of a signed S/MIME message, defined in [RFC 4262](https://datatracker.ietf.org/doc/html/rfc4262).

j. `subjectDirectoryAttributes` (optional)

   | Generation | `subjectDirectoryAttributes`      | 
   |------|-----------------------|
   | Strict and Multipurpose | Prohibited |
   | Legacy | MAY be present and MUST NOT be marked critical. |

   May contain verified attributes which are not part of the Subject's Distinguished Name such as dateOfBirth, placeOfBirth, gender, countryOfCitizenship, or countryOfResidence in accordance with [RFC 3739 Section 3.2.2](https://tools.ietf.org/html/rfc3739#section-3.2.2). 

k. qcStatements (optional)

   This extension MAY be present and MUST NOT be marked critical. Indicates a Certificate that is issued as Qualified within a defined legal framework from an identified country or set of countries in accordance with [RFC 3739 Section 3.2.6](https://tools.ietf.org/html/rfc3739#section-3.2.6) and ETSI EN 319 412-5, Section 4.

l. Legal Entity Identifier (optional)

   | Generation | LEI      | 
   |------|-----------------------|
   | Mailbox-validated | Prohibited |
   | Organization-validated | LEI (1.3.6.1.4.1.52266.1) MAY be present and MUST NOT be marked critical.  |
   | Sponsored-validated | LEI (1.3.6.1.4.1.52266.1) or for role (1.3.6.1.4.1.52266.2) MAY be present and MUST NOT be marked critical.  |
   | Individual-validated | Prohibited |

   LEI data records are used in accordance with ISO 17442-1:2020, Clause 6 and ISO 17442-2:2020, Clause 4.

   The CA MUST verify that the RegistrationStatus for the LEI record is ISSUED and the EntityStatus is ACTIVE.  The CA SHALL only allow use of an LEI if the ValidationSources entry is FULLY_CORROBORATED; an LEI MUST NOT be used if ValidationSources entry is PARTIALLY_CORROBORATED, PENDING, or ENTITY_SUPPLIED_ONLY.

m. Adobe Extensions (optional)

   | Generation | Adobe Extensions      | 
   |------|-----------------------|
   | Strict | Prohibited |
   | Multipurpose and Legacy | MAY be present and MUST NOT be marked critical. May include the Adobe Time-stamp X509 extension (1.2.840.113583.1.1.9.1) or the Adobe ArchiveRevInfo extension (1.2.840.113583.1.1.9.2) |

#### 7.1.2.4 All certificates

All fields and extensions MUST be set in accordance with RFC 5280. The CA SHALL NOT issue a Certificate that contains a `keyUsage` flag, `extKeyUsage` value, Certificate extension, or other data not specified in [Section 7.1.2.1](#7121-root-ca-certificate), [Section 7.1.2.2](#7122-subordinate-ca-certificate), or [Section 7.1.2.3](#7123-subscriber-certificates) unless the CA is aware of a reason for including the data in the Certificate.

CAs SHALL NOT issue a Certificate with:

1. Extensions that do not apply in the context of the public Internet (such as an extKeyUsage value for a service that is only valid in the context of a privately managed network), unless:<br>
   i. such value falls within an OID arc for which the Applicant demonstrates ownership, or<br>
   ii. the Applicant can otherwise demonstrate the right to assert the data in a public context; or
2. semantics that, if included, will mislead a Relying Party about the Certificate information verified by the CA (such as including an `extKeyUsage` value for a smart card, where the CA is not able to verify that the corresponding Private Key is confined to such hardware due to remote issuance).
   
### 7.1.3 Algorithm object identifiers

#### 7.1.3.1 SubjectPublicKeyInfo

The following requirements apply to the `subjectPublicKeyInfo` field within a Certificate. No other encodings are permitted.

##### 7.1.3.1.1 RSA

The CA SHALL indicate an RSA key using the rsaEncryption (OID: 1.2.840.113549.1.1.1) algorithm identifier. The parameters MUST be present, and MUST be an explicit NULL.
The CA SHALL NOT use a different algorithm, such as the id-RSASSA-PSS (OID: 1.2.840.113549.1.1.10) algorithm identifier, to indicate an RSA key.

When encoded, the `AlgorithmIdentifier` for RSA keys MUST be byte-for-byte identical with the following hex-encoded bytes: `300d06092a864886f70d0101010500`

##### 7.1.3.1.2 ECDSA

The CA SHALL indicate an ECDSA key using the id-ecPublicKey (OID: 1.2.840.10045.2.1) algorithm identifier. The parameters MUST use the `namedCurve` encoding.

* For P-256 keys, the `namedCurve` MUST be secp256r1 (OID: 1.2.840.10045.3.1.7).
* For P-384 keys, the `namedCurve` MUST be secp384r1 (OID: 1.3.132.0.34).
* For P-521 keys, the `namedCurve` MUST be secp521r1 (OID: 1.3.132.0.35).

When encoded, the `AlgorithmIdentifier` for ECDSA keys MUST be byte-for-byte identical with the following hex-encoded bytes:

* For P-256 keys, `301306072a8648ce3d020106082a8648ce3d030107`.
* For P-384 keys, `301006072a8648ce3d020106052b81040022`.
* For P-521 keys, `301006072a8648ce3d020106052b81040023`.

##### 7.1.3.1.3 EdDSA

The CA SHALL indicate an EdDSA key using one of the following algorithm identifiers below:

* For curve25519 keys, the `algorithm` MUST be id-Ed25519 (OID: 1.3.101.112).
* For curve448 keys, the `algorithm` MUST be id-Ed448 (OID: 1.3.101.113).

The parameters for EdDSA keys MUST be absent.

When encoded, the `AlgorithmIdentifier` for EdDSA keys MUST be byte-for-byte identical with the following hex-encoded bytes:

* For Curve25519 keys, `300506032b6570`.
* For Curve448 keys, `300506032b6571`.

#### 7.1.3.2 Signature AlgorithmIdentifier

All objects signed by a CA Private Key MUST conform to these requirements on the use of the `AlgorithmIdentifier` or `AlgorithmIdentifier`-derived type in the context of signatures.

In particular, it applies to all of the following objects and fields:

* The `signatureAlgorithm` field of a Certificate.
* The `signature` field of a TBSCertificate (for example, as used by a Certificate).
* The `signatureAlgorithm` field of a CertificateList
* The `signature` field of a TBSCertList
* The `signatureAlgorithm` field of a BasicOCSPResponse.

No other encodings are permitted for these fields.

##### 7.1.3.2.1 RSA

The CA SHALL use one of the following signature algorithms and encodings. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the specified hex-encoded bytes.

* RSASSA-PKCS1-v1_5 with SHA-256:

  Encoding:
  `300d06092a864886f70d01010b0500`.

* RSASSA-PKCS1-v1_5 with SHA-384:

  Encoding:
  `300d06092a864886f70d01010c0500`.

* RSASSA-PKCS1-v1_5 with SHA-512:

  Encoding:
  `300d06092a864886f70d01010d0500`.

* RSASSA-PSS with SHA-256, MGF-1 with SHA-256, and a salt length of 32 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040201
  0500a11c301a06092a864886f70d010108300d0609608648016503040201
  0500a203020120
  ```

* RSASSA-PSS with SHA-384, MGF-1 with SHA-384, and a salt length of 48 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040202
  0500a11c301a06092a864886f70d010108300d0609608648016503040202
  0500a203020130
  ```

* RSASSA-PSS with SHA-512, MGF-1 with SHA-512, and a salt length of 64 bytes:

  Encoding:

  ```hexdump
  304106092a864886f70d01010a3034a00f300d0609608648016503040203
  0500a11c301a06092a864886f70d010108300d0609608648016503040203
  0500a203020140
  ```

##### 7.1.3.2.2 ECDSA

The CA SHALL use the appropriate signature algorithm and encoding based upon the signing key used.

If the signing key is P-256, the signature MUST use ECDSA with SHA-256. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040302`.

If the signing key is P-384, the signature MUST use ECDSA with SHA-384. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040303`.

If the signing key is P-521, the signature MUST use ECDSA with SHA-512. When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300a06082a8648ce3d040304`.

##### 7.1.3.2.3 EdDSA

The CA SHALL use the appropriate signature algorithm and encoding based upon the signing key used.

If the signing key is Curve25519, the signature algorithm MUST be id-Ed25519 (OID: 1.3.101.112). When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300506032b6570`.

If the signing key is Curve448, the signature algorithm MUST be id-Ed448 (OID: 1.3.101.113). When encoded, the `AlgorithmIdentifier` MUST be byte-for-byte identical with the following hex-encoded bytes: `300506032b6571`.

### 7.1.4 Name forms

Attribute values SHALL be encoded according to [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280).

#### 7.1.4.1 Name encoding

For every valid Certification Path (as defined by [RFC 5280, Section 6](https://datatracker.ietf.org/doc/html/rfc5280#section-6)):

* For each Certificate in the Certification Path, the encoded content of the Issuer Distinguished Name field of a Certificate SHALL be byte-for-byte identical with the encoded form of the Subject Distinguished Name field of the Issuing CA Certificate.
* For each CA Certificate in the Certification Path, the encoded content of the Subject Distinguished Name field of a Certificate SHALL be byte-for-byte identical among all Certificates whose Subject Distinguished Names can be compared as equal according to [RFC 5280, Section 7.1](https://datatracker.ietf.org/doc/html/rfc5280#section-7.1), and including expired and revoked Certificates.

#### 7.1.4.2 Subject information - subscriber certificates

By issuing the Certificate, the CA represents that it followed the procedure set forth in its CP and/or CPS to verify that, as of the Certificate's issuance date, all of the Subject Information was accurate. 

CAs SHALL NOT include an email address in a Subject attribute except as verified in accordance with [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control)

Subject attributes MUST NOT contain only metadata such as '.', '-', and ' ' (i.e. space) characters, and/or any other indication that the value is absent, incomplete, or not applicable. 

##### 7.1.4.2.1 Subject alternative name extension

__Certificate Field:__ `extensions:subjectAltName`  
__Required/Optional:__ MUST be present  
__Contents:__ This extension MUST contain at least one entry of the following types:

* `Rfc822Name` and/or
* `otherName` of type `id-on-SmtpUTF8Mailbox`

All Subject email attribute values contained in the Subject MUST be repeated in this extension. In addition the following apply:

   | Generation | `keyUsage`      | 
   |------|-----------------------|
   | Strict | MUST NOT contain `otherNames` other than type `id-on-SmtpUTF8Mailbox`. |
   | Multipurpose and Legacy | `otherName` values MAY be included. `otherNames` of type `id-on-SmtpUTF8Mailbox` MUST be encoded in accordance with [RFC 8398](https://datatracker.ietf.org/doc/html/rfc8398). `otherNames` MUST be validated in accordance with procedures documented in the CA's CP and/or CPS.|

This extension MUST NOT contain items of type `dNSName`, `iPAddress`,  `uniformResourceIdentifier`, or `GeneralNames` of any other type.

##### 7.1.4.2.2 Subject distinguished name fields

a. __Certificate Field:__ `subject:commonName` (OID 2.5.4.3)  
   __Contents:__ If present, this attribute MUST contain one of the following values verified in accordance with [Section 3.2](#32-initial-identity-validation).

| Type    | Contents |
|---------|----------|
| Mailbox-validated | `subject:emailAddress` |
| Organization-validated | `subject:organizationName` or `subject:emailAddress` |
| Sponsored-validated | Personal Name, `subject:pseudonym`, or `subject:emailAddress` |
| Individual-validated | Personal Name, `subject:pseudonym`, or `subject:emailAddress` |

If present, the Personal Name SHALL contain a name of the Subject. The Personal Name SHOULD be presented as `subject:givenName` and/or `subject:surname`. The Personal Name MAY be in the Subject's preferred presentation format or a format preferred by the CA or Enterprise RA, but SHALL be a meaningful representation of the Subject’s name as verified under [Section 3.2.4](#324-authentication-of-individual-identity). 

Note: `subject:commonName` and `subject:emailAddress` SHALL comply with the attribute upper bounds defined in [RFC 5280](https://datatracker.ietf.org/doc/html/rfc5280).

Additional specifications for naming are provided in [Section 3.1](#31-naming).

b. __Certificate Field:__ `subject:organizationName` (OID 2.5.4.10)  
   __Contents:__ If present, the `subject:organizationName` field MUST contain the Subject's full legal organization name as verified under [Section 3.2.3](#323-authentication-of-organization-identity). The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name". 
   
   An assumed name used by the Subject as verified under [Section 3.2.3.2](#3232-verification-of-organization-assumed-name) MAY be included at the beginning of this field, provided that it is followed by the full legal organization name in parenthesis.

c. __Certificate Field:__ `subject:organizationalUnitName` (OID: 2.5.4.11)  
   __Contents:__ If present, the CA SHALL confirm that the `subject:organizationalUnitName` is the full legal organization name of an Affiliate of the `subject:organizationName` in the Certificate and has been verified in accordance with the requirements of [Section 3.2](#32-initial-identity-validation). The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations.

d. __Certificate Field:__ `subject:organizationIdentifier` (2.5.4.97)  
   __Contents:__ If present, the `subject:organizationIdentifier` field MUST contain a Registration Reference for a Legal Entity assigned in accordance to the identified Registration Scheme. 

   The organizationIdentifier MUST be encoded as a PrintableString or UTF8String.

   The Registration Scheme identified in the Certificate MUST be the result of the verification performed in accordance with [Section 3.2.3](#323-authentication-of-organization-identity). The Registration Scheme MUST be identified using the using the following structure in the presented order:

    * 3 character Registration Scheme identifier;
    * 2 character ISO 3166 country code for the nation in which the Registration Scheme is operated, or if the scheme is operated globally ISO 3166 code "XG" SHALL be used;
    * For the NTR Registration Scheme identifier, if required under [Section 9.2.4](#924-subject-jurisdiction-of-incorporation-or-registration-field), a 2 character ISO 3166-2 identifier for the subdivision (state or province) of the nation in which the Registration Scheme is operated, preceded by plus "+" (0x2B (ASCII), U+002B (UTF-8));
    * a hyphen-minus "-" (0x2D (ASCII), U+002D (UTF-8));
    * Registration Reference allocated in accordance with the identified Registration Scheme

   Note: Registration References MAY contain hyphens, but Registration Schemes, ISO 3166 country codes, and ISO 3166-2 identifiers do not. Therefore if more than one hyphen appears in the structure, the leftmost hyphen is a separator, and the remaining hyphens are part of the Registration Reference.

   Examples:

    * `NTRGB-12345678` (NTR scheme, Great Britain, Unique Identifier at Country level is 12345678)
    * `NTRUS+CA-12345678` (NTR Scheme, United States - California, Unique identifier at State level is 12345678)
    * `VATDE-123456789` (VAT Scheme, Germany, Unique Identifier at Country Level is 12345678)
    * `PSDBE-NBB-1234.567.890` (PSD Scheme, Belgium, NCA's identifier is NBB, Subject Unique Identifier assigned by the NCA is 1234.567.890)

   Registration Schemes listed in [Appendix A](#appendix-a---registration-schemes) are recognized as valid under these guidelines.

   The CA SHALL:

   1. confirm that the organization represented by the Registration Reference is the same as the organization named in the `organizationName` field as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields);
   2. further verify the Registration Reference matches other information verified in accordance with [Section 3.2.3](#323-authentication-of-organization-identity);
   3. take appropriate measures to disambiguate between different organizations as described in [Appendix A](#appendix-a---registration-schemes)) for each Registration Scheme;
   4. Apply the validation rules relevant to the Registration Scheme as specified in [Appendix A](#appendix-a---registration-schemes).

e. __Certificate Field:__ `subject:givenName` (2.5.4.42) and/or `subject:surname` (2.5.4.4)  
   __Contents:__ If present, the `subject:givenName` field and `subject:surname` field MUST contain a natural person Subject’s name as verified under [Section 3.2.4](#324-authentication-of-individual-identity). Subjects with a single legal name SHALL provide the name in the `subject:surname` attribute. The `subject:givenName` and/or `subject:surname` MUST NOT be present if the `subject:pseudonym` is present.

f. __Certificate Field:__ `subject:pseudonym` (2.5.4.65)  
   __Contents:__ The `subject:pseudonym` MUST NOT be present if the `subject:givenName` and/or `subject:surname` are present. If present, the `subject:pseudonym` field MUST be verified according to [Section 3.1.3](#313-anonymity-or-pseudonymity-of-subscribers).

g. __Certificate Field:__ `subject:serialNumber` (2.5.4.5) 
   __Contents:__ If present, the `subject:serialNumber` MAY be used to contain an identifier assigned by the CA or RA to identify and/or to disambiguate the Subscriber.

h. __Certificate Field:__ `subject:emailAddress` (1.2.840.113549.1.9.1) 
   __Contents:__ If present, the `subject:emailAddress` MUST contain a single `Rfc822Name` or an `otherName` of type `id-on-SmtpUTF8Mailbox` as verified under [Section 3.2.2](#322-validation-of-mailbox-authorization-or-control)

i. __Certificate Field:__ `subject:title` (2.5.4.12) 
   __Contents:__ If present, the `subject:title` field MUST contain only a corporate role/title or a regulated professional designation verified according to [Section 3.2.4](#324-authentication-of-individual-identity).

j. __Certificate Field:__ Number and street: `subject:streetAddress` (OID: 2.5.4.9)  
 __Contents:__ If present, the `subject:streetAddress` field MUST contain the Subject's street address information as verified under [Section 3.2.3](#323-authentication-of-organization-identity) or [Section 3.2.4](#324-authentication-of-individual-identity).

k. __Certificate Field:__ `subject:localityName` (OID: 2.5.4.7)  
   __Required__ if the `subject:organizationName`, or the `subject:givenName` and/or `subject:surname` fields, are present and the `subject:stateOrProvinceName` field is absent.
   __Optional__ if the `subject:stateOrProvinceName` field is present. 
   __Contents:__ If present, the `subject:localityName` field MUST contain the Subject's locality information as verified under [Section 3.2.3](#323-authentication-of-organization-identity) or [Section 3.2.4](#324-authentication-of-individual-identity). If the `subject:countryName` field specifies the ISO 3166-1 user-assigned code of XX in accordance with [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) (g), the `localityName` field MAY contain the Subject's locality and/or state or province information.

l. __Certificate Field:__ `subject:stateOrProvinceName` (OID: 2.5.4.8)  
   __Required__ if the `subject:organizationName`, or the `subject:givenName` and/or `subject:surname` fields, are present and the `subject:localityName` field is absent.
   __Optional__ if the `subject:localityName` field is present. 
   __Contents:__ If present, the `subject:stateOrProvinceName` field MUST contain the Subject's state or province information as verified under [Section 3.2.3](#323-authentication-of-organization-identity) or [Section 3.2.4](#324-authentication-of-individual-identity). If the `subject:countryName` field specifies the ISO 3166-1 user-assigned code of XX in accordance with [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields) (g), the `subject:stateOrProvinceName` field MAY contain the full name of the Subject's country information.

m. __Certificate Field:__ `subject:postalCode` (OID: 2.5.4.17)  
   __Contents:__ If present, the `subject:postalCode` field MUST contain the Subject's zip or postal information as verified under [Section 3.2.3](#323-authentication-of-organization-identity) or [Section 3.2.4](#324-authentication-of-individual-identity)

n. __Certificate Field:__ `subject:countryName` (OID: 2.5.4.6)  
   __Contents:__ If present, the `subject:countryName` MUST contain the two-letter ISO 3166-1 country code associated with the location of the Subject verified under [Section 3.2.3](#323-authentication-of-organization-identity) or [Section 3.2.4](#324-authentication-of-individual-identity). If a Country is not represented by an official ISO 3166-1 country code, the CA MAY specify the ISO 3166-1 user-assigned code of XX indicating that an official ISO 3166-1 alpha-2 code has not been assigned.

##### 7.1.4.2.3 Subject DN attributes for mailbox-validated profile

| Attribute | Legacy | Multipurpose | Strict |
|-----------|--------|--------------|--------|
| `subject:commonName` | MAY  | MAY | MAY |
| `subject:organizationName` | MUST NOT | MUST NOT | MUST NOT |
| `subject:organizationalUnitName` | MUST NOT | MUST NOT | MUST NOT |
| `subject:organizationIdentifier` | MUST NOT | MUST NOT | MUST NOT |
| `subject:givenName` | MUST NOT | MUST NOT | MUST NOT |
| `subject:surname` | MUST NOT | MUST NOT | MUST NOT |
| `subject:pseudonym` | MUST NOT | MUST NOT | MUST NOT |
| `subject:serialNumber` | MAY | MAY | MAY |
| `subject:emailAddress` | MAY | MAY | MAY |
| `subject:title` | MUST NOT | MUST NOT | MUST NOT |
| `subject:streetAddress` | MUST NOT | MUST NOT | MUST NOT |
| `subject:localityName` | MUST NOT | MUST NOT | MUST NOT |
| `subject:stateOrProvinceName` | MUST NOT | MUST NOT | MUST NOT |
| `subject:postalCode` | MUST NOT | MUST NOT | MUST NOT |
| `subject:countryName` | MUST NOT | MUST NOT | MUST NOT |
| Other | MUST NOT | MUST NOT | MUST NOT |

##### 7.1.4.2.3 Subject DN attributes for organization-validated profile

| Attribute | Legacy | Multipurpose | Strict |
|-----------|--------|--------------|--------|
| `subject:commonName` | MAY  | MAY | MAY |
| `subject:organizationName` | MUST | MUST | MUST |
| `subject:organizationalUnitName` | MAY  | MAY | MAY |
| `subject:organizationIdentifier` | MUST | MUST | MUST |
| `subject:givenName` | MUST NOT | MUST NOT | MUST NOT |
| `subject:surname` | MUST NOT | MUST NOT | MUST NOT |
| `subject:pseudonym` | MUST NOT | MUST NOT | MUST NOT |
| `subject:serialNumber` | MAY | MAY | MAY |
| `subject:emailAddress` | MAY | MAY | MAY |
| `subject:title` | MUST NOT | MUST NOT | MUST NOT |
| `subject:streetAddress` | MAY | MAY | MUST NOT |
| `subject:localityName` | MAY | MAY | MAY |
| `subject:stateOrProvinceName` | MAY | MAY | MAY |
| `subject:postalCode` | MAY | MAY | MUST NOT |
| `subject:countryName` | MAY | MUST | MUST |
| Other | MAY | MUST NOT | MUST NOT |

##### 7.1.4.2.4 Subject DN attributes for sponsor-validated profile

| Attribute | Legacy | Multipurpose | Strict |
|-----------|--------|--------------|--------|
| `subject:commonName` | MAY  | MAY | MAY |
| `subject:organizationName` | MUST | MUST | MUST |
| `subject:organizationalUnitName` | MAY  | MAY | MAY |
| `subject:organizationIdentifier` | MUST | MUST | MUST |
| `subject:givenName` | MAY  | MAY | MAY |
| `subject:surname` | MAY  | MAY | MAY |
| `subject:pseudonym` | MAY | MAY | MAY |
| `subject:serialNumber` | MAY | MAY | MAY |
| `subject:emailAddress` | MAY | MAY | MAY |
| `subject:title` | MAY  | MAY | MAY |
| `subject:streetAddress` | MAY | MAY | MUST NOT |
| `subject:localityName` | MAY | MAY | MAY |
| `subject:stateOrProvinceName` | MAY | MAY | MAY |
| `subject:postalCode` | MAY | MAY | MUST NOT |
| `subject:countryName` | MAY | MUST | MUST |
| Other | MAY | MUST NOT | MUST NOT |

The `Sponsor-validated` profile MUST include either `subject:givenName` and/or `subject:surname`, or the `subject:pseudonym`.

##### 7.1.4.2.5 Subject DN attributes for individual-validated profile

| Attribute | Legacy | Multipurpose   | Strict |
|-----------|--------|----------------|--------|
| `subject:commonName` | MAY  | MAY | MAY |
| `subject:organizationName` | MUST NOT | MUST NOT | MUST NOT |
| `subject:organizationalUnitName` | MUST NOT | MUST NOT | MUST NOT |
| `subject:organizationIdentifier` | MUST NOT | MUST NOT | MUST NOT |
| `subject:givenName` | MAY  | MAY | MAY |
| `subject:surname` | MAY  | MAY | MAY |
| `subject:pseudonym` | MAY | MAY | MAY |
| `subject:serialNumber` | MAY | MAY | MAY |
| `subject:emailAddress` | MAY | MAY | MAY |
| `subject:title` | MAY  | MAY | MAY |
| `subject:streetAddress` | MAY | MAY | MUST NOT |
| `subject:localityName` | MAY | MAY | MAY |
| `subject:stateOrProvinceName` | MAY | MAY | MAY |
| `subject:postalCode` | MAY | MAY | MUST NOT |
| `subject:countryName` | MAY | MUST | MUST |
| Other | MAY | MUST NOT | MUST NOT |

The `Individual-validated` profile MUST include either `subject:givenName` and/or `subject:surname`, or the `subject:pseudonym`.

#### 7.1.4.3 Subject information - root certificates and subordinate CA certificates

By issuing a Subordinate CA Certificate, the CA represents that it followed the procedure set forth in its CP and/or CPS to verify that, as of the Certificate's issuance date, all of the Subject Information was accurate.

##### 7.1.4.3.1 Subject distinguished name fields

a. __Certificate Field:__ `subject:commonName` (OID 2.5.4.3)  
   __Required/Optional:__ MUST be present  
   __Contents:__ This field MUST be present and the contents SHOULD be an identifier for the Certificate such that the Certificate's Name is unique across all Certificates issued by the Issuing CA.

b. __Certificate Field:__ `subject:organizationName` (OID 2.5.4.10)  
   __Required/Optional:__ MUST be present  
   __Contents:__ This field MUST be present and the contents MUST contain either the Subject CA's name or DBA as verified under [Section 3.2.3.3](#3233-verification-of-applicants-legal-existence-and-identity--assumed-name) The CA MAY include information in this field that differs slightly from the verified name, such as common variations or abbreviations, provided that the CA documents the difference and any abbreviations used are locally accepted abbreviations; e.g., if the official record shows "Company Name Incorporated", the CA MAY use "Company Name Inc." or "Company Name".

c. __Certificate Field:__ `subject:countryName` (OID: 2.5.4.6)  
   __Required/Optional:__ MUST be present  
   __Contents:__ This field MUST contain the two‐letter ISO 3166‐1 country code for the country in which the CA's place of business is located.

d. Other Subject Attributes  
   Other attributes MAY be present within the subject field. If present, other attributes MUST contain information that has been verified by the CA.

### 7.1.5 Name constraints

For a Subordinate CA Certificate to be considered Technically Constrained, the Certificate MUST include an Extended Key Usage (EKU) extension specifying all extended key usages for which the Subordinate CA Certificate is authorized to issue Certificates. The `anyExtendedKeyUsage` KeyPurposeId MUST NOT appear within this extension.

If the Subordinate CA Certificate includes the `id-kp-emailProtection` extended key usage, then for the Subordinate CA Certificate to be considered Technically Constrained it MUST include the `nameConstraints` X.509v3 extension with constraints on `rfc822Name` and `directoryName` as follows:

   1. For each `rfc822Name` in `permittedSubtrees`, each `rfc822Name` MUST contain either a FQDN or a U+002E FULL STOP (".") character followed by a FQDN. The `rfc822Name` MUST NOT contain an email address. The CA MUST confirm that the Applicant has registered the FQDN contained in the `rfc822Name` or has been authorized by the domain registrant to act on the registrant's behalf in line with the verification practices of [Section 3.2.2.3](#3223-validating-applicant-as-operator-of-associated-mail-servers).

   2. For each `directoryName` in `permittedSubtrees`, the CA MUST confirm the Applicant's and/or Subsidiary's Organizational name and location such that end entity Certificates issued from the Subordinate CA Certificate will be in compliance with [Section 7.1.2.4](#7124-all-certificates).

### 7.1.6 Certificate policy object identifier

This section describes the content requirements for the Root CA, Subordinate CA, and Subscriber Certificates as they relate to the identification of Certificate Policy.

#### 7.1.6.1 Reserved certificate policy identifiers

The following CA/Browser Forum Certificate Policy identifiers are reserved for use by CAs to assert that a Certificate complies with these Requirements.

| Validation Type | Generation | Policy Identifier |
| ---------------- | ---------- | ----------------- |
| Mailbox-validated | Legacy | `2.23.140.1.5.1.1` |
| Mailbox-validated | Multipurpose | `2.23.140.1.5.1.2` |
| Mailbox-validated | Strict | `2.23.140.1.5.1.3` |
| Organization-validated | Legacy | `2.23.140.1.5.2.1` |
| Organization-validated | Multipurpose | `2.23.140.1.5.2.2` |
| Organization-validated | Strict | `2.23.140.1.5.2.3` |
| Sponsor-validated | Legacy | `2.23.140.1.5.3.1` |
| Sponsor-validated | Multipurpose | `2.23.140.1.5.3.2` |
| Sponsor-validated | Strict | `2.23.140.1.5.3.3` |
| Individual-validated | Legacy | `2.23.140.1.5.4.1` |
| Individual-validated | Multipurpose | `2.23.140.1.5.4.2` |
| Individual-validated | Strict | `2.23.140.1.5.4.3` |

#### 7.1.6.2 Root CA certificates

A Root CA Certificate SHOULD NOT contain the `certificatePolicies` extension. If present, the extension MUST conform to the requirements set forth for Certificates issued to Subordinate CAs in [Section 7.1.6.3](#7163-subordinate-ca-certificates).

#### 7.1.6.3 Subordinate CA certificates

A Certificate issued to a Subordinate CA that is not an Affiliate of the Issuing CA:

1. MUST include one or more explicit policy identifiers defined in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) that indicate the Subordinate CA's adherence to and compliance with these Requirements and MAY contain one or more identifiers documented by the Subordinate CA in its CP and/or CPS; and
2. MUST NOT contain the `anyPolicy` identifier (2.5.29.32.0).

A Certificate issued to a Subordinate CA that is an Affiliate of the Issuing CA MUST include a set of policy identifiers from one of the two options below:

1. MUST include one or more explicit policy identifiers defined in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers) that indicate the Subordinate CA's adherence to and compliance with these Requirements and MAY contain one or more identifiers documented by the Subordinate CA in its CP and/or CPS; or
2. MUST contain the `anyPolicy` identifier (2.5.29.32.0).

The Subordinate CA and the Issuing CA SHALL represent, in their CP and/or CPS, that all Certificates containing a policy identifier indicating compliance with these Requirements are issued and managed in accordance with these Requirements.

#### 7.1.6.4 Subscriber certificates

A Certificate issued to a Subscriber MUST contain, within the Certificate's `certificatePolicies` extension, a policy identifier that is specified in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers).

The Certificate MAY also contain additional policy identifier(s) defined by the Issuing CA. The Issuing CA SHALL document in its CP and/or CPS that the Certificates it issues containing the specified policy identifier(s) are managed in accordance with these Requirements.

### 7.1.7 Usage of policy constraints extension

No stipulation.

### 7.1.8 Policy qualifiers syntax and semantics

No stipulation.

### 7.1.9 Processing semantics for the critical certificate policies extension

No stipulation.

## 7.2 CRL profile

### 7.2.1 Version number(s)

No stipulation.

### 7.2.2 CRL and CRL entry extensions

If present, the `reasonCode` (OID 2.5.29.21) extension MUST NOT be marked critical.

If a CRL entry is for a Root CA or Subordinate CA Certificate, including Cross Certificates, this CRL entry extension MUST be present. If a CRL entry is for a Certificate not technically capable of causing issuance, this CRL entry extension SHOULD be present, but MAY be omitted, subject to the following requirements.

The `CRLReason` indicated MUST NOT be unspecified (0). If the reason for revocation is unspecified, CAs MUST omit `reasonCode` entry extension. The `CRLReason` MUST NOT be certificateHold (6).

If a `reasonCode` CRL entry extension is present, the `CRLReason` MUST indicate the most appropriate reason for revocation of the Certificate, as defined by the CA within its CP/CPS.

## 7.3 OCSP profile

If an OCSP response is for a Root CA or Subordinate CA Certificate, including Cross Certificates, and that Certificate has been revoked, then the `revocationReason` field within the `RevokedInfo` of the `CertStatus` MUST be present.

The `CRLReason` indicated MUST contain a value permitted for CRLs, as specified in [Section 7.2.2](#722-crl-and-crl-entry-extensions).

### 7.3.1 Version number(s)

No stipulation.

### 7.3.2 OCSP extensions

The `singleExtensions` of an OCSP response MUST NOT contain the `reasonCode` (OID 2.5.29.21) CRL entry extension.

# 8. COMPLIANCE AUDIT AND OTHER ASSESSMENTS

The CA SHALL at all times:

1. Issue Certificates and operate its PKI in accordance with all law applicable to its business and the Certificates it issues in every jurisdiction in which it operates;
2. Comply with these Requirements;
3. Comply with the audit requirements set forth in this section; and
4. Be licensed as a CA in each jurisdiction where it operates, if licensing is required by the law of such jurisdiction for the issuance of Certificates.

**Implementers' Note**: The CA/Browser Forum continues to improve the S/MIME Baseline Requirements while WebTrust and ETSI also continue to update their audit criteria. We encourage all CAs to conform to each revision herein on the date specified without awaiting a corresponding update to an applicable audit criterion. In the event of a conflict between an existing audit criterion and a revision to the S/MIME Baseline Requirements, we will communicate with the audit community and attempt to resolve any uncertainty, and we will respond to implementation questions directed to <questions@cabforum.org>. 

## 8.1 Frequency or circumstances of assessment

Certificates that are capable of being used to issue new Certificates MUST either be Technically Constrained in line with [Section 7.1.5](#715-name-constraints) and audited in line with [Section 8.8](#88-review-of-enterprise-ra-or-technically-constrained-subordinate-ca) only, or Unconstrained and fully audited in line with all remaining requirements from this section. A Certificate is deemed as capable of being used to issue new Certificates if it contains an X.509v3 `basicConstraints` extension, with the `cA` boolean set to true and is therefore by definition a Root CA Certificate or a Subordinate CA Certificate.

The period during which the CA issues Certificates SHALL be divided into an unbroken sequence of audit periods. An audit period MUST NOT exceed one year in duration.

If the CA has a currently valid Audit Report indicating compliance with an audit scheme listed in [Section 8.4](#84-topics-covered-by-assessment), then no pre-issuance readiness assessment is necessary.

If the CA does not have a currently valid Audit Report indicating compliance with one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment), then, before issuing Publicly-Trusted S/MIME Certificates, the CA SHALL successfully complete a point-in-time readiness assessment performed in accordance with applicable standards under one of the audit schemes listed in [Section 8.4](#84-topics-covered-by-assessment). The point-in-time readiness assessment SHALL be completed no earlier than twelve (12) months prior to issuing Publicly-Trusted S/MIME Certificates and SHALL be followed by a complete audit under such scheme within ninety (90) days of issuing the first Publicly-Trusted S/MIME Certificate.

## 8.2 Identity/qualifications of assessor

The CA's audit SHALL be performed by a Qualified Auditor. A Qualified Auditor means a natural person, Legal Entity, or group of natural persons or Legal Entities that collectively possess the following qualifications and skills:

1. Independence from the subject of the audit;
2. The ability to conduct an audit that addresses the criteria specified in an Eligible Audit Scheme (see [Section 8.4](#84-topics-covered-by-assessment));
3. Employs individuals who have proficiency in examining Public Key Infrastructure technology, information security tools and techniques, information technology and security auditing, and the third-party attestation function;
4. (For audits conducted in accordance with any one of the ETSI standards) accredited in accordance with ISO 17065 applying the requirements specified in ETSI EN 319 403;
5. (For audits conducted in accordance with the WebTrust standard) licensed by WebTrust;
6. Bound by law, government regulation, or professional code of ethics; and
7. Except in the case of an Internal Government Auditing Agency, maintains Professional Liability/Errors & Omissions insurance with policy limits of at least one million US dollars in coverage.
   
## 8.3 Assessor's relationship to assessed entity

No stipulation.

## 8.4 Topics covered by assessment

The CA SHALL undergo an audit in accordance with one of the following schemes:

1. “WebTrust for CAs v2.2.1 or newer” AND “WebTrust for S/MIME Baseline Requirements vX.X.X or newer”; or
2. "ETSI EN 319 411-1 v1.3.1 or newer", which includes normative references to ETSI EN 319 401 (the latest version of referenced ETSI documents should be applied); or
3. If a Government CA is required by its Certificate Policy to use a different internal audit scheme, it MAY use such scheme provided that the audit either
   a. encompasses all requirements of one of the above schemes or
   b. consists of comparable criteria that are available for public review.
Whichever scheme is chosen, it MUST incorporate periodic monitoring and/or accountability procedures to ensure that its audits continue to be conducted in accordance with the requirements of the scheme.

The audit MUST be conducted by a Qualified Auditor, as specified in [Section 8.2](#82-identityqualifications-of-assessor).

For Delegated Third Parties that are not Enterprise RAs, then the CA SHALL obtain an audit report, issued under the auditing standards that underlie the accepted audit schemes found in [Section 8.4](#84-topics-covered-by-assessment), that provides an opinion whether the Delegated Third Party's performance complies with either the Delegated Third Party's practice statement or the CA's CP and/or CPS. If the opinion is that the Delegated Third Party does not comply, then the CA SHALL not allow the Delegated Third Party to continue performing delegated functions.

The audit period for the Delegated Third Party SHALL NOT exceed one year (ideally aligned with the CA's audit). However, if the CA or Delegated Third Party is under the operation, control, or supervision of a Government Entity and the audit scheme is completed over multiple years, then the annual audit MUST cover at least the core controls that are required to be audited annually by such scheme plus that portion of all non-core controls that are allowed to be conducted less frequently, but any non-core control SHALL NOT be audited less often than once every three years.

## 8.5 Actions taken as a result of deficiency

No stipulation.

## 8.6 Communication of results

The Audit Report SHALL state explicitly that it covers the relevant systems and processes used in the issuance of all Certificates that assert one or more of the policy identifiers listed in [Section 7.1.6.1](#7161-reserved-certificate-policy-identifiers). The CA SHALL make the Audit Report publicly available.

The CA MUST make its Audit Report publicly available no later than three months after the end of the audit period. In the event of a delay greater than three months, the CA SHALL provide an explanatory letter signed by the Qualified Auditor.

The Audit Report MUST contain at least the following clearly-labelled information:

1. Name of the organization being audited;
2. Name and address of the organization performing the audit;
3. The SHA-256 fingerprint of all Roots and Subordinate CA Certificates, including Cross Certificates, that were in-scope of the audit;
4. Audit criteria, with version number(s), that were used to audit each of the Certificates (and associated keys);
5. A list of the CA policy documents, with version numbers, referenced during the audit;
6. Whether the audit assessed a period of time or a point in time;
7. The start date and end date of the Audit Period, for those that cover a period of time;
8. The point in time date, for those that are for a point in time;
9. The date the report was issued, which will necessarily be after the end date or point in time date; 
10. (For audits conducted in accordance with any of the ETSI standards) a statement to indicate if the audit was a full audit or a surveillance audit, and which portions of the criteria were applied and evaluated, e.g., ETSI EN 319 401, ETSI EN 319 411-1 policy LCP, NCP or NCP+, ETSI EN 319 411-2 policy QCP-n, QCP-n-qscd, QCP-l or QCP-l-qscd; and
11. (For audits conducted in accordance with any of the ETSI standards) a statement to indicate that the auditor referenced the applicable CA/Browser Forum criteria, such as this document, and the version used.

An authoritative English language version of the publicly available audit information MUST be provided by the Qualified Auditor and the CA SHALL ensure it is publicly available.

The Audit Report MUST be available as a PDF, and SHALL be text searchable for all information required. Each SHA-256 fingerprint within the Audit Report MUST be uppercase letters and MUST NOT contain colons, spaces, or line feeds.

## 8.7 Self audits

During the period in which the CA issues Certificates, the CA SHALL monitor adherence to its CP and/or CPS and these Requirements and control its service quality by performing self audits on at least a quarterly basis against a randomly selected sample including a minimum of the greater of thirty (30) Certificates or three percent (3%) of the Certificates issued by it during the period commencing immediately after the previous self-audit sample was taken. 

## 8.8 Review of delegated parties 

Except for Delegated Third Parties, Enterprise RAs, and Technically Constrained Subordinate CAs that undergo an annual audit that meets the criteria specified in [Section 8.4](#84-topics-covered-by-assessment), the CA SHALL ensure the practices and procedures of each Delegated Third Party, Enterprise RA, and Technically Constrained Subordinate CA are in compliance with these Requirements and the relevant CP and/or CPS. The CA shall document the obligations of Delegated Third Parties, Enterprise RAs, and Technically Constrained Subordinate CAs and perform internal audits of their adherence with those obligations on an annual basis.

# 9. OTHER BUSINESS AND LEGAL MATTERS

## 9.1 Fees

### 9.1.1 Certificate issuance or renewal fees

No stipulation.

### 9.1.2 Certificate access fees

No stipulation.

### 9.1.3 Revocation or status information access fees

No stipulation.

### 9.1.4 Fees for other services

No stipulation.

### 9.1.5 Refund policy

No stipulation.

## 9.2 Financial responsibility

### 9.2.1 Insurance coverage

No stipulation.

### 9.2.2 Other assets

No stipulation.

### 9.2.3 Insurance or warranty coverage for end-entities

No stipulation.

## 9.3 Confidentiality of business information

### 9.3.1 Scope of confidential information

No stipulation.

### 9.3.2 Information not within the scope of confidential information

No stipulation.

### 9.3.3 Responsibility to protect confidential information

No stipulation.

## 9.4 Privacy of personal information

### 9.4.1 Privacy plan

No stipulation.

### 9.4.2 Information treated as private

If a Certificate includes the `subject:pseudonym` attribute, the CA or Enterprise RA that performed the validation of the Individual in accordance with [Section 3.2.4](#324-authentication-of-individual-identity) MUST treat information that links the Pseudonym to the real identity of the Subject of the Certificate as private. Disclosure requirements of this information SHALL follow applicable laws in the CA or Enterprise RA's jurisdiction. 

### 9.4.3 Information not deemed private

No stipulation.

### 9.4.4 Responsibility to protect private information

No stipulation.

### 9.4.5 Notice and consent to use private information

No stipulation.

### 9.4.6 Disclosure pursuant to judicial or administrative process

No stipulation.

### 9.4.7 Other information disclosure circumstances

No stipulation.

## 9.5 Intellectual property rights

No stipulation.

## 9.6 Representations and warranties

### 9.6.1 CA representations and warranties

By issuing a Certificate, the CA makes the warranties listed herein to the following Certificate Beneficiaries:

1.  The Subscriber that is a party to the Subscriber Agreement or Terms of Use for the Certificate;
2.  All Application Software Suppliers with whom the Root CA has entered into a contract for inclusion of its Root CA Certificate in software distributed by such Application Software Supplier; and
3.  All Relying Parties who reasonably rely on a Valid Certificate. 

The CA represents and warrants to the Certificate Beneficiaries that, during the period when the Certificate is valid, the CA has complied with these Requirements and its CP and/or CPS in issuing and managing the Certificate.

The Certificate Warranties specifically include, but are not limited to, the following:

1. **Right to Use Domain Name or Email Address**: That, at the time of issuance, the CA:
   i. implemented a procedure for verifying that the Applicant either had the right to use, or had control of, the Domain Name(s) and email mailbox(es) listed in the Certificate's `subject` field and `subjectAltName` extension (or was delegated such right or control by someone who had such right to use or control);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
2. **Authorization for Certificate**: That, at the time of issuance, the CA:
   i. implemented a procedure for verifying that the Subject authorized the issuance of the Certificate and that the Applicant Representative is authorized to request the Certificate on behalf of the Subject;
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
3. **Accuracy of Information**: That, at the time of issuance, the CA:
   i. implemented a procedure for verifying the accuracy of all of the information contained in the Certificate (with the exception of the subject:serialNumber attribute);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
4. **Identity of Applicant**: That, if the Certificate contains Subject Identity Information, the CA:
   i. implemented a procedure to verify the identity of the Applicant in accordance with [Section 3.2](#32-initial-identity-validation) and [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields);
   ii. followed the procedure when issuing the Certificate; and
   iii. accurately described the procedure in the CA's CP and/or CPS;
5. **Subscriber Agreement**: That, if the CA and Subscriber are not Affiliated, the Subscriber and CA are parties to a legally valid and enforceable Subscriber Agreement that satisfies these Requirements, or, if the CA and Subscriber are the same entity or are Affiliated, the Applicant Representative acknowledged the Terms of Use;
6. **Status**: That the CA maintains a 24 x 7 publicly-accessible Repository with current information regarding the status (Valid or Revoked) of all unexpired Certificates; and
7. **Revocation**: That the CA will revoke the Certificate for any of the reasons specified in these Requirements.

The Root CA SHALL be responsible for the performance and warranties, compliance with these Requirements, and for all liabilities and indemnification obligations of the Subordinate CA under these Requirements, as if the Root CA were the Subordinate CA issuing the Certificates

### 9.6.2 RA representations and warranties

No stipulation.

### 9.6.3 Subscriber representations and warranties

The CA SHALL require, as part of the Subscriber Agreement or Terms of Use, that the Applicant make the commitments and warranties in this section for the benefit of the CA and the Certificate Beneficiaries.

Prior to the issuance of a Certificate, the CA SHALL obtain, for the express benefit of the CA and the Certificate Beneficiaries, either the Applicant's:

1. Agreement to the Subscriber Agreement with the CA; or
2. Acknowledgement of the Terms of Use.

The CA SHALL implement a process to ensure that each Subscriber Agreement or Terms of Use is legally enforceable against the Applicant. In either case, the Agreement MUST apply to the Certificate to be issued pursuant to the Certificate Request. The CA MAY use an electronic or "click-through" Agreement provided that the CA has determined that such agreements are legally enforceable. A separate Agreement MAY be used for each Certificate Request, or a single Agreement MAY be used to cover multiple future Certificate Requests and the resulting Certificates, so long as each Certificate that the CA issues to the Applicant is clearly covered by that Subscriber Agreement or Terms of Use.

The Subscriber Agreement or Terms of Use MUST contain provisions imposing on the Applicant itself (or made by the Applicant on behalf of its principal or agent under a subcontractor or hosting service relationship) the following obligations and warranties:

1. **Accuracy of Information**: An obligation and warranty to provide accurate and complete information at all times to the CA, both in the certificate request and as otherwise requested by the CA in connection with the issuance of the Certificate(s) to be supplied by the CA;
2. **Protection of Private Key**: An obligation and warranty by the Applicant to take all reasonable measures to assure control of, keep confidential, and properly protect at all times the Private Key that corresponds to the Public Key to be included in the requested Certificate(s) (and any associated activation data or device, e.g. password or token);
3. **Acceptance of Certificate**: An obligation and warranty that the Subscriber will review and verify the Certificate contents for accuracy;
4. **Use of Certificate**: An obligation and warranty to use the Certificate only on email mailboxes listed in the Certificate, and to use the Certificate solely in compliance with all applicable laws and solely in accordance with the Subscriber Agreement or Terms of Use;
5. **Reporting and Revocation**: An obligation and warranty to:
   a. promptly request revocation of the Certificate, and cease using it and its associated Private Key, if there is any actual or suspected misuse or compromise of the Subscriber’s Private Key associated with the Public Key included in the Certificate, and
   b. promptly request revocation of the Certificate, and cease using it, if any information in the Certificate is or becomes incorrect or inaccurate;
6. **Termination of Use of Certificate**: An obligation and warranty to promptly cease all use of the Private Key corresponding to the Public Key included in the Certificate upon revocation of that Certificate for reasons of Key Compromise.
7. **Responsiveness**: An obligation to respond to the CA's instructions concerning Key Compromise or Certificate misuse within a specified time period.
8. **Acknowledgment and Acceptance**: An acknowledgment and acceptance that the CA is entitled to revoke the Certificate immediately if the Applicant were to violate the terms of the Subscriber Agreement or Terms of Use, or if revocation is required by the CA's CP and/or CPS, or by these Requirements.


### 9.6.4 Relying party representations and warranties

No stipulation.

### 9.6.5 Representations and warranties of other participants

No stipulation.

## 9.7 Disclaimers of warranties

No stipulation.

## 9.8 Limitations of liability

For delegated tasks, the CA and any Delegated Third Party MAY allocate liability between themselves contractually as they determine, but the CA SHALL remain fully responsible for the performance of all parties in accordance with these Requirements, as if the tasks had not been delegated.

If the CA has issued and managed the Certificate in compliance with these Requirements and its CP and/or CPS, the CA MAY disclaim liability to the Certificate Beneficiaries or any other third parties for any losses suffered as a result of use or reliance on such Certificate beyond those specified in the CA's CP and/or CPS. If the CA has not issued or managed the Certificate in compliance with these Requirements and its CP and/or CPS, the CA MAY seek to limit its liability to the Subscriber and to Relying Parties, regardless of the cause of action or legal theory involved, for any and all claims, losses or damages suffered as a result of the use or reliance on such Certificate by any appropriate means that the CA desires. If the CA chooses to limit its liability for Certificates that are not issued or managed in compliance with these Requirements or its CP and/or CPS, then the CA SHALL include the limitations on liability in the CA's CP and/or CPS.

## 9.9 Indemnities

Notwithstanding any limitations on its liability to Subscribers and Relying Parties, the CA understands and acknowledges that the Application Software Suppliers who have a Root CA Certificate distribution agreement in place with the Root CA do not assume any obligation or potential liability of the CA under these Requirements or that otherwise might exist because of the issuance or maintenance of Certificates or reliance thereon by Relying Parties or others. Thus, except in the case where the CA is a government entity, the CA SHALL defend, indemnify, and hold harmless each Application Software Supplier for any and all claims, damages, and losses suffered by such Application Software Supplier related to a Certificate issued by the CA, regardless of the cause of action or legal theory involved. This does not apply, however, to any claim, damages, or loss suffered by such Application Software Supplier related to a Certificate issued by the CA where such claim, damage, or loss was directly caused by such Application Software Supplier's software displaying as not trustworthy a Certificate that is still valid, or displaying as trustworthy: (1) a Certificate that has expired, or (2) a Certificate that has been revoked (but only in cases where the revocation status is currently available from the CA online, and the application software either failed to check such status or ignored an indication of revoked status).

## 9.10 Term and termination

### 9.10.1 Term

No stipulation.

### 9.10.2 Termination

No stipulation.

### 9.10.3 Effect of termination and survival

No stipulation.

## 9.11 Individual notices and communications with participants

No stipulation.

## 9.12 Amendments

### 9.12.1 Procedure for amendment

No stipulation.

### 9.12.2 Notification mechanism and period

No stipulation.

### 9.12.3 Circumstances under which OID must be changed

No stipulation.

## 9.13 Dispute resolution provisions

No stipulation.

## 9.14 Governing law

No stipulation.

## 9.15 Compliance with applicable law

No stipulation.

## 9.16 Miscellaneous provisions

### 9.16.1 Entire agreement

No stipulation.

### 9.16.2 Assignment

No stipulation.

### 9.16.3 Severability

In the event of a conflict between these Requirements and a law, regulation or government order (hereinafter ‘Law’) of any jurisdiction in which a CA operates or issues Certificates, a CA MAY modify any conflicting requirement to the minimum extent necessary to make the requirement valid and legal in the jurisdiction. This applies only to operations or Certificate issuances that are subject to that Law. In such event, the CA SHALL immediately (and prior to issuing a Certificate under the modified requirement) include in Section 9.16.3 of the CA’s CPS a detailed reference to the Law requiring a modification of these Requirements under this section, and the specific modification to these Requirements implemented by the CA.

The CA SHALL also (prior to issuing a Certificate under the modified requirement) notify the CA/Browser Forum of the relevant information newly added to its CPS by sending a message to <public@cabforum.org> and receiving confirmation that it has been posted to the Public Mailing List and is indexed in the Public Mail Archives available at [https://cabforum.org/pipermail/public/](https://cabforum.org/pipermail/public/) (or such other email addresses and links as the Forum may designate), so that the CA/Browser Forum may consider possible revisions to these Requirements accordingly.

Any modification to CA practice enabled under this section SHALL be discontinued if and when the Law no longer applies, or these Requirements are modified to make it possible to comply with both them and the Law simultaneously. An appropriate change in practice, modification to the CA’s CPS and a notice to the CA/Browser Forum, as outlined above, SHALL be made within 90 days.

### 9.16.4 Enforcement (attorneys' fees and waiver of rights)

No stipulation.

### 9.16.5 Force majeure

No stipulation.

## 9.17 Other provisions

 No stipulation.

# Appendix A - Registration schemes

The following Registration Schemes are recognized as valid under these guidelines:

* **NTR**:

  For an identifier allocated by a national trade register to a Legal Entity. The country code used in the Registration Scheme identifier SHALL match that of the subject’s jurisdiction in the `subject:countryName` as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).

* **VAT**:

  For an identifier allocated by the national tax authorities to a Legal Entity. This information SHALL be validated using information provided by the national tax authority for the entity named in the `subject:organizationName` within the context of the subject’s jurisdiction in the `subject:countryName` as specified in as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).

* **PSD**:

  For an authorization number as specified in ETSI TS 119 495 clause 4.4
  allocated to a payment service provider and containing the information as
  specified in ETSI TS 119 495 clause 5.2.1.  This information SHALL be
  obtained directly from the national competent authority register for
  payment services or from an information source approved by a government
  agency, regulatory body, or legislation for this purpose. 
  
  This information SHALL be validated for the entity named in the `subject:organizationName` and registration number within the context of the subject’s jurisdiction in the `subject:countryName` as specified in as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).
  
  This information SHALL be validated by being matched directly or indirectly (for example, by matching a globally unique registration number) against the entity named in the `subject:organizationName` within the context of the subject’s jurisdiction in the `subject:countryName` as specified in as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields).
  The stated address of the organization combined with the organization name
  SHALL NOT be the only information used to disambiguate the organization.

* **LEI**:

  For a global Legal Entity Identifier as specified in ISO 17442 for the entity named in the `subject:organizationName` as specified in [Section 7.1.4.2.2](#71422-subject-distinguished-name-fields). The 2 character ISO 3166 country code SHALL be set to 'XG'. 

  The CA MUST verify that the RegistrationStatus for the LEI record is ISSUED and the EntityStatus is ACTIVE.  The CA SHALL only allow use of an LEI if the ValidationSources entry is FULLY_CORROBORATED; an LEI MUST NOT be used if ValidationSources entry is PARTIALLY_CORROBORATED, PENDING, or ENTITY_SUPPLIED_ONLY.

# Appendix B - Country-specific interpretative guidelines (normative)

NOTE: This appendix provides alternative interpretations of these Requirements for countries that have a language, cultural, technical, or legal reason for deviating from a strict interpretation of these Requirements. More specific information for particular countries may be added to this appendix in the future.

## 1. Organization names

1. Non-Latin Organization Name

   Where an Applicant's organization name is not registered with a QGIS in _Latin_ characters and the Applicant's non-Latin character organization name and registration have been verified with a QGIS in accordance with these Requirements, a CA MAY include a Latin character organization name in the Certificate. In such a case, the CA MUST follow the procedures laid down in this section.

2. Romanized Names

   In order to include a transliteration/Romanization of the registered name, the Romanization MUST be verified by the CA using a system officially recognized by the Government in the Applicant's Jurisdiction of Incorporation.

   If the CA can not rely on a transliteration/Romanization of the registered name using a system officially recognized by the Government in the Applicant's Jurisdiction of Incorporation, then it MUST rely on one of the options below, in order of preference:

   A.  A system recognized by the International Organization for Standardization (ISO);
   B.  A system recognized by the United Nations; or
   C.  A Lawyer's Opinion or Accountant's Letter confirming the proper Romanization of the registered name.

3. Translated Name

   In order to include a Latin character name in the Certificate that is not a direct Romanization of the registered name (e.g. an English Name)  the CA MUST verify that the Latin character name is:

   A.  Included in the Articles of Incorporation (or equivalent document) filed as part of the organization registration; or
   B.  Recognized by a QTIS in the Applicant's Jurisdiction of Incorporation as the Applicant's recognized name for tax filings; or
   C.  Confirmed with a QIIS to be the name associated with the registered organization; or
   D.  Confirmed by a Verified Legal Opinion or Accountant's Letter to be a translated trading name associated with the registered organization.

### Country-specific procedures

#### B-1. Japan

As interpretation of the procedures set out above:

1. Organization Names

   A.  The Revised Hepburn method of Romanization, as well as Kunrei-shiki and Nihon-shiki methods described in ISO 3602, are acceptable for Japanese Romanizations.
   B.  The CA MAY verify the Romanized transliteration, language translation (e.g. English name), or other recognized Roman-letter substitute of the Applicant's formal legal name with either a QIIS, Verified Legal Opinion, or Verified Accountant Letter.
   C.  The CA MAY use the Financial Services Agency to verify a Romanized, translated, or other recognized Roman-letter substitute name. When used, the CA MUST verify that the translated English is recorded in the audited Financial Statements.
   D.  When relying on Articles of Incorporation to verify a Romanized, translated, or other recognized Roman-letter substitute name, the Articles of Incorporation MUST be accompanied either: by a document, signed with the original Japanese Corporate Stamp, that proves that the Articles of Incorporation are authentic and current, or by a Verified Legal Opinion or a Verified Accountant Letter. The CA MUST verify the authenticity of the Corporate Stamp.
   E.  A Romanized, translated, or other recognized Roman-lettered substitute name confirmed in accordance with this [Appendix B-1](#b-1-japan) stored in the ROBINS database operated by JIPDEC MAY be relied upon by a CA for determining the allowed organization name during any issuance or renewal process of a Certificate without the need to re-perform the above procedures.

2. Accounting Practitioner

   In Japan:

   A.  Accounting Practitioner includes either a certified public accountant (公認会計士 - Konin-kaikei-shi) or a licensed tax accountant (税理士 – Zei-ri-shi).
   B.  The CA MUST verify the professional status of the Accounting Practitioner through direct contact with the relevant local member association that is Affiliated with either the Japanese Institute of Certified Public Accountants ([http://www.hp.jicpa.or.jp](http://www.hp.jicpa.or.jp/)), the Japan Federation of Certified Tax Accountant's Associations ([http://www.nichizeiren.or.jp](http://www.nichizeiren.or.jp/)), or any other authoritative source recognized by the Japanese Ministry of Finance ([http://www.mof.go.jp](http://www.mof.go.jp/)) as providing the current registration status of such professionals.

3. Legal Practitioner

   In Japan:

   A.  Legal Practitioner includes any of the following:

       - a licensed lawyer (弁護士 - Ben-go-shi),
       - a judicial scrivener (司法書士 - Shiho-sho-shi lawyer),
       - an administrative solicitor (行政書士 - Gyosei-sho-shi Lawyer),
       - or a notary public (公証人 - Ko-sho-nin).

       For purposes of these Requirements, a Japanese Notary Public is considered equivalent to a Latin Notary.

   B.  The CA MUST verify the professional status of the Legal Practitioner by direct contact through the relevant local member association that is Affiliated with one of the following national associations:

       - the Japan Federation of Bar Associations ([http://www.nichibenren.or.jp](http://www.nichibenren.or.jp/)),
       - the Japan Federation of Shiho-Shoshi Lawyer's Associations ([http://www.shiho-shoshi.or.jp](http://www.shiho-shoshi.or.jp/)),
       - the Japan Federation of Administrative Solicitors ([http://www.gyosei.or.jp](http://www.gyosei.or.jp/)),
       - the Japan National Notaries Association ([http://www.koshonin.gr.jp](http://www.koshonin.gr.jp/)), or
       - any other authoritative source recognized by the Japanese Ministry of Justice ([http://www.moj.go.jp](http://www.moj.go.jp/)) as providing the current registration status of such professionals.
