package org.vimpiarte.store.dataAccess.models;

import jakarta.persistence.*;
import lombok.*;

import java.util.*;

@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@ToString
@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "email", nullable = false)
    private String email;

    @Column(name = "password", nullable = false)
    private String password;

    @OneToMany(mappedBy = "user")
    @Builder.Default // needed to initialize the list when using the builder
    private List<Address> addresses = new ArrayList<>();

    @OneToOne(mappedBy = "user")
    private Profile profile;

    // The User model is the 'owner' of the relationship
    // in One-to-many relationships, the 'owner' is usually the table
    // with the foreign key, but with M2M, either could be.
    @ManyToMany
    @JoinTable(
            name = "user_tags", // the name of the through table
            joinColumns = @JoinColumn(name = "user_id"),
            inverseJoinColumns = @JoinColumn(name = "tag_id")
    )
    @Builder.Default // need this if we're going to use the @Builder annotation
    private Set<Tag> tags = new HashSet<>();

    public void addAddress(Address address) {
        addresses.add(address);
        address.setUser(this);
    }

    /**
     * Add a tag from a string/tag name
     */
    public void addTag(String name) {
        var tag = new Tag(name);
        tags.add(tag);
        tag.getUsers().add(this);
    }

}
