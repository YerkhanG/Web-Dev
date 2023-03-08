import { Component,OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {Album} from "../models";
import {Photos} from "../photos";
import {AlbumService} from "../album.service";

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit {
  album : Album;
  photos: Photos[];
  constructor(private route: ActivatedRoute, private albumService: AlbumService) {
    this.album = {} as Album;
    this.photos = [{}] as Photos[];
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe(
      (params) => {
        let _id = params.get('id');
        if (_id) {
          let id = +_id;
          this.albumService.getAlbum(id).subscribe(
            (response) => {
              this.album = response;
            },
            (error) => {
              console.log(error);
            }
          );
          this.albumService.getPhotos(id).subscribe(
            (response) => {
              this.photos = response;
            },
            (error) => {
              console.log(error);
            }
          );
        }
      }
    );
  }

  back() {
    window.location.href = `http://localhost:4200/albums/${this.album.id}`;
  }
}
